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
        db = self.mongo_client.VOIP
        self.collection = db.Users

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
            answer = (self.collection.find({"login": login, "password": password, "activated":"true"}).count()) == 1

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

        msg['Subject'] = 'JaroEliCall: kod aktywacyjny użytkownika'
        msg['From'] = me
        msg['To'] = to

        body_text = "Informacja: Aby zakończyć rejestracje należy użyć" \
                    " poniższego kodu jako hasła.\n ### Kod aktywacyjny do" \
                    " konta: " + activ_code + "### \n" \
                    " Prosimy nie odpowiadać na tą wiadomość"

        msg['Body'] = body_text

        server = smtplib.SMTP('localhost')
        server.starttls()

        server.sendmail(me, to, msg.as_string())
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
