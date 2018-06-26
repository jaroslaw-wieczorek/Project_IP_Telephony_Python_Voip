from sys import platform
from pymongo import MongoClient
import os


class MongoOperations:

    def __init__(self):
        self.dict_ip_users = {}

        if platform == "linux" or platform == "linux2":
            print("POLACZENIE Z MONGO")
        else:
            print("POLACZENIE Z MONGO")
            os.startfile("C:/Program Files/MongoDB/Server/3.6/bin/mongod.exe")

    def runMongo(self):
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
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

    def getFromMongo(self):
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']
        users = []

        for user in collection.find({}, {"login": 1, "status": 1, "_id": 0}):
            users.append(user)
            print("Dodano: " + str(user))
        print("Lista: " + str(users))
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
            answer = (self.collection.find({"login": login, "password": password}).count()) == 1
            print(answer)
            if (answer):
                self.collection.update({"login": login, "password": password}, {"$set": {"status": "online"}})
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
            answer = (self.collection.find({"login": user, "status": "online"}).count()) == 1
            if (answer):
                return True
            else:
                return False

        except IndexError:
            return False

    def create_user(self, login, email, password):
        print("Dodanie uzytkowwnika do mongo")
        try:
            self.collection.insertOne({"login": login, "password": password, "status": "offline"})
        except IndexError:
            return 0

    def get_username_from_ip(self, addr):
        print("Adres",  addr)
        # słownik {'EKaczmarek': adres IP}
        for i in self.dict_ip_users:
            print(i)

    def logoutUser(self, addr):
        nickname = self.get_username_from_ip(addr)
        self.runMongo()
        self.getFromMongo()
        try:
            self.collection.update_one({"login": nickname}, {"$set": {"status": "offline"}})
            self.getFromMongo()
            return 1

        except IndexError:
            return 0