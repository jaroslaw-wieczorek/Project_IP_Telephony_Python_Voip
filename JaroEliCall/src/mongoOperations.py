import os
import sys
import string
import random
import smtplib
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

    def check_if_login_unique(self, login):
        print("Sprawdzenie z mongo")
        self.runMongo()
        try:
            answer = (self.collection.find({"login": login}).count()) == 0
            if answer:
                return True
            else:
                return False

        except IndexError:
            return False

    def check_if_email_exists(self, email):
        print("Sprawdzenie z mongo")
        self.runMongo()
        try:
            answer = (self.collection.find({"email": email}).count()) >= 1
            if (answer):
                return True
            else:
                return False

        except IndexError:
            return False

    def change_password_mongo(self, login, password):
        try:
            answer = (self.collection.find({"login": login}).count()) == 1

            print(answer)
            if answer:
                self.collection.update(
                    {
                        "login": login
                    },
                    {
                        "$set": {"password": password}
                    })

                # to dictionary nickname adres IP
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

        for user in collection.find({}, {"login": 1, "status": 1, "_id": 0, "avatar": 1}):
            users.append(user)
        self.users = users
        print("self.users ", self.users)

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

        # , "status": "offline"

        try:
            answer = (self.collection.find({"login": login, "password": password}).count()) == 1

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
                return True
            else:

                return False

        except IndexError:
            return False

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

        answer_mongo = hashlib.sha256(result_mongo.encode()).hexdigest()
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
        
        me = "tt0815550@gmail.com"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(me, "AureliaK1609")

        msg = MIMEMultipart()
        msg['Subject'] = "JaroEliCall - rejestracja użytkownika " + str(to)
        msg["From"] = me
        msg["To"] = to
        body_text = "Informacja: Aby zakonczyć rejestracje nalezy uzyc ponizszego kodu jako hasla.\n\n Kod aktywacyjny do konta: " + str(activ_code) + "\n Prosimy nie odpowiadac na ta wiadomosc"

        msg.attach(MIMEText(body_text, "plain"))

        server.sendmail("tt0815550@gmail.com", to, msg.as_string())
        server.quit()

    def create_user(self, login, email):
        print("loginL ", login)
        print("email: ", email)

        activation_code = self.createActivationCode(ACTIVATION_CODE_LENGHT)
        password = hashlib.sha256(activation_code.encode()).hexdigest()
        print("Dodanie uzytkowwnika do mongo")

        try:
            self.collection.insert_one({"email": email,
                                        "login": login,
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
