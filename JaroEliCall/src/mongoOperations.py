import os
import sys
import string
import random

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pymongo import MongoClient
from itsdangerous import BadSignature
from itsdangerous import URLSafeSerializer
import hashlib

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

ACTIVATION_CODE_LENGHT = 24

class MongoOperations:

    MongoIP, MongoPort = ("127.0.0.1", 27017)

    def __init__(self):
        self.dict_ip_users = {}

        if sys.platform == "linux" or sys.platform == "linux2":
            print("POLACZENIE Z MONGO")
        else:
            print("POLACZENIE Z MONGO")
            os.startfile("C:/Program Files/MongoDB/Server/3.6/bin/mongod.exe")

    def connectMongo(self):
        print("POLACZENIE Z MONGO istnieje")

    def runMongo(self):
        self.mongo_client = MongoClient(self.MongoIP, self.MongoPort)
        db = self.mongo_client['VOIP']
        self.collection = db['Users']

    def find_in_mongo(self, login):
        print("Sprawdzenie z mongo")
        self.runMongo()
        try:
            answer = (self.collection.find({"login": login}).count()) >= 1
            if (answer):
                return 0
            else:
                return 1

        except IndexError:
            return 0

    def check_if_email_exists(self, email):
        print("Sprawdzenie z mongo")
        self.runMongo()
        try:
            answer = (self.collection.find({"login": email}).count()) >= 1
            if (answer):
                return True
            else:
                return False

        except IndexError:
            return False

    def getFromMongo(self):
        client = MongoClient(self.MongoIP, self.MongoPort)
        db = client['VOIP']
        collection = db['Users']
        users = []

        for user in collection.find({}, {"login": 1, "status": 1, "_id": 0}):
            users.append(user)
        self.users = users

    def logoutAll(self):
        self.runMongo()
        test = [list(self.collection.find({}, {"login": 1, "status": 1, "_id": 0})) for self.collection in
                self.collection_names()]
        for i in test:
            print(i)

    def checkWithMongo(self, login, password, addr):
        self.runMongo()

        print("Login", login)
        print("Password", password)
        try:
            answer = (self.collection.find({"login": login, "password": password, "status": "offline"}).count()) == 1

            print(answer)
            if answer:
                self.collection.update(
                    {
                        "login": login,
                        "password": password
                    },
                    {
                        "$set": {"status": "online"}
                    })

                # to dictionary nickname adres IP
                self.dict_ip_users[login] = addr
                return 1
            else:

                return 0

        except IndexError:
            return 0

    def check_is_account_activated(self, login):
        activated = self.collection.find({"login": login}, {"activated": 1})
        ans = False
        for i in activated:
            ans = (i['activated'])

        return ans

    def check_if_login_exists(self, login):
        if self.collection.find({'login': login}).count() > 0:
            return True
        else:
            return False

    def check_login_code(self, login, password_my):
        password_mongo = self.collection.find({"login": login}, {"activation_code": 1})

        result_mongo = ''
        for i in password_mongo:
            result_mongo = i["activation_code"]

        print("Pobrano z bazy haslo: ", result_mongo)
        print("Wpisano haslo o skrocie: ", password_my)

        answer_mongo = hashlib.sha256(result_mongo.encode()).hexdigest()
        print()
        print(answer_mongo)
        return password_my == answer_mongo

    def update_mongo_activate(self, login):
        password_mongo = self.collection.find({"login": login}, {"activation_code": 1})

        id_mongo = ''
        for i in password_mongo:
            id_mongo = i["_id"]

        self.collection.update(
             {"_id": id_mongo},
                {"$set":
                {
                    "activated": True
                }
            }
        )
        result = self.collection.find({"_id": id_mongo, "login": login},
                                      {"activation_code": 1, "login": login, "activation_code": 1})
        for i in result:
            print(i)
        print("koniec")

    def checkAvailibility(self, user):
        self.runMongo()
        try:
            answer = (self.collection.find({
                                            "login": user,
                                            "status": "online"
                                            }).count()) == 1
            if (answer):
                return True
            else:
                return False

        except IndexError:
            return False

    def createActivationCode(self, length):
        return ''.join(random.sample(string.ascii_letters +
                                     string.digits +
                                     string.punctuation, length))

    def sendActivationCode(self, activ_code, to):
        msg = MIMEMultipart()
        me = "JaroEliCall"

        msg['Subject'] = str(me) +': kod aktywacyjny użytkownika'
        msg['From'] = str(me)
        msg['To'] = str(to)

        body_text = "Informacja: Aby zakończyć rejestracje należy użyć " \
                    "poniższego kodu jako hasła.\n\n### Kod aktywacyjny do " \
                    "konta: " + str(activ_code) + " ### \n" \
                    "Prosimy nie odpowiadać na tą wiadomość"

        msg.attach(MIMEText(body_text, 'plain'))
        server = smtplib.SMTP("localhost")
        server.starttls()
        print("Set debug")
        server.set_debuglevel(True)

        server.sendmail(me, to, msg.as_string())
        print("SENDED EMAIL!!!", me, to, msg.as_string())

        server.quit()

    def create_user(self, login, email, password):
        print("loginL ", login)
        print("email: ", email)
        print("password ", password)
        print("Dodanie uzytkowwnika do mongo")

        activation_code = self.createActivationCode(ACTIVATION_CODE_LENGHT)
        try:
            self.collection.insert_one({"login": login,
                                        "password": password,
                                        "status": "offline",
                                        "activated": False,
                                        "activation_code": activation_code})

            self.sendActivationCode(activation_code, email)
        except IndexError:
            return 0

    # zwraca nazwę użytkownika na podstawie jego IP
    def get_username_from_ip(self, addr):
        for key, value in self.dict_ip_users.items():
            if(value == addr):
                return key

    # wylogowanie użytkownika mając jest adres IP oraz port w tupli addr
    def logoutUser(self, addr):
        nickname = self.get_username_from_ip(addr)
        self.runMongo()
        self.getFromMongo()
        print("Nickname usera: ", nickname)
        try:
            self.collection.update_one({"login": nickname}, {"$set": {"status": "offline"}})
            self.getFromMongo()
            return 1
        except IndexError:
            return 0
