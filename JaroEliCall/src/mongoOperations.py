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

        test = [list(db[collection].find({}, {"login": 1, "status": 1, "_id": 0})) for collection in
                db.collection_names()]
        self.users = test

    def logoutAll(self):
        self.runMongo()
        test = [list(self.collection.find({}, {"login": 1, "status": 1, "_id": 0})) for self.collection in
                self.collection_names()]
        for i in test:
            print(i)

    def checkWithMongo(self, data, addr):
        self.runMongo()

        print(data)
        frames = (data.split())

        try:
            answer = (self.collection.find({"login": frames[3], "password": frames[4]}).count()) == 1
            print(answer)
            if (answer):
                self.collection.update({"login": frames[3], "password": frames[4]}, {"$set": {"status": "online"}})
                # to dictionary nickname adres IP
                self.dict_ip_users[frames[3]] = addr
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
                return 1
            else:
                return 0

        except IndexError:
            return 0

    def create_user(self, login, email, password):
        print("Dodanie uzytkowwnika do mongo")
        try:
            self.collection.insertOne({"login": login, "password": password, "status": "offline"})
        except IndexError:
            return 0

    def logoutUser(self, addr):
        nickname = self.get_username_from_ip(addr)
        self.runMongo()
        self.getFromMongo()
        try:
            answer = self.collection.update_one({"login": nickname}, {"$set": {"status": "offline"}})
            self.getFromMongo()
            return 1

        except IndexError:
            return 0