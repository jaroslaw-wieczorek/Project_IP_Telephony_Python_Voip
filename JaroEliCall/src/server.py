import pyaudio
import socket
from pymongo import MongoClient
# from validation import Validator
import os
import json
import time

from sys import platform


# class Server(Validator):
class Server:
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 15
    FACTOR = 2

    dict_ip_users = {}

    def __init__(self):

        # Validator.__init__(self, priv, publ)
        print("Inicjalizacja klasy Server")

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

    def connectWithMongo(self):

        if platform == "linux" or platform == "linux2":
            print("POLACZENIE Z MONGO")
                        
            
        elif platform == "win32":
            print("POLACZENIE Z MONGO")
            os.startfile("C:/Program Files/MongoDB/Server/3.6/bin/mongod.exe")

    def connectWithClient(self):
        print("Nawiazanie polaczenia")
        self.host = ''
        self.port = 50001
        self.size = 2048

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.bind((self.host, self.port))
        except ConnectionRefusedError as err:
            print(err)
            self.s.close()

    def sendAnything(self, addr):

        while 1:
            time.sleep(2)
            self.s.sendto(("Hello to ja").encode("utf-8"), addr)
            break

    def listening(self):
        print("[*] Start listen")

        while 1:
            d, addr = self.s.recvfrom(self.size*2)
            print("Otrzymalem: ", d, " od ", addr)
            data = d[0:1].decode("utf-8")
            if (data[0:1] == "d"):

                communicate = d.decode("utf-8")
                print("Komunikat: ", communicate[7:12])

                print(communicate)
                if(communicate[2:7]=="LOGIN"):
                    print("Otrzymano LOGIN")
                    ans = self.checkWithMongo(communicate, addr)
                    if (ans == 1):
                        print('Wysylanie 200')
                        self.s.sendto(("200 OK").encode("utf-8"), addr)
                        print('Wysłano 200')

                    elif (ans == 0):
                        print('Wysylanie 406')
                        self.s.sendto(("406 NOT ACCEPTABLE").encode("utf-8"), addr)
                        print('Wyslano 406')

                elif (communicate[2:5] == "GET"):
                    print("Otrzymano GET")
                    self.getFromMongo()
                    print("Wysylanie userow")

                    self.s.sendto(("202" + json.dumps(self.users)).encode("utf-8"), addr)
                    print("Wyslano userow")

                elif (communicate[2:8] == "INVITE"):
                    frames = (communicate.split())
                    print(communicate)
                    print("Mam zadzwonic do", frames[2])
                    ans = self.checkAvailibility(frames[2])
                    print("frames[2] = ", frames[2])
                    # print(ans, " ", self.dict_ip_users[frames[2]])
                    if (ans):
                        self.s.sendto(("200 OK ").encode("utf-8"), (addr[0],50003))
                    else:
                        self.s.sendto(("460 NOT ACCEPTABLE").encode("utf-8"), (addr[0],50003))
                elif(communicate[6:12]=="CREATE"):
                    frames = (communicate.split())
                    print("Tworzenie usera:", frames[4])
                    ans = self.find_in_mongo(frames[4])
                    print(addr)
                    if(ans == 1):
                        self.create_user(frames[4], frames[3], frames[5])
                        self.s.sendto(("201 CREATED").encode("utf-8"), addr)
                    elif(ans == 0):
                        self.s.sendto(("406 NOT ACCEPTABLE").encode("utf-8"), addr)
            elif (data[0:1]=="s"):
                print("Dzwiek: ")
                self.stream.write(d[2:])

        print("[*] Stop listen")

    def create_user(self, login, email, password):
        print("Dodanie uzytkowwnika do mongo")

        try:
            self.collection.insertOne({"login": login, "password":password, "status": "offline"})
        except IndexError:
            return 0

    def find_in_mongo(self, login):
        print("Sprawdzenie z mongo")
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        self.collection = db['Users']

        try:
            answer = (self.collection.find({"login": login}).count()) >=1
            if (answer):
                return 0
            else:
                return 1

        except IndexError:
            return 0

    def checkAvailibility(self, user):
        print("Sprawdzenie z mongo")
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']

        try:
            answer = (collection.find({"login": user, "status": "online"}).count()) == 1
            if (answer):
                return 1
            else:
                return 0

        except IndexError:
            return 0

    def stopConnection(self):
        self.stream.stop_stream()
        self.stream.close()

        self.s.close()

        # p.close()

    def checkWithMongo(self, data, addr):
        print("Sprawdzenie z mongo")
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']

        print(data)
        frames = (data.split())

        try:
            answer = (collection.find({"login": frames[3], "password": frames[4]}).count()) == 1

            if (answer):
                collection.update({"login": frames[3], "password": frames[4]}, {"$set": {"status": "online"}})
                # to dictionary nickname        adres IP
                self.dict_ip_users[frames[3]] = addr
                return 1
            else:
                return 0

        except IndexError:
            return 0

    def getFromMongo(self):
        self.users = {}

        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']
        try:
            answer = collection.find({})
            for document in answer:
                self.users["login"] = document["login"]
                self.users["status"] = document["status"]
        except IndexError:
            return 0

        print(self.users)


"""

priv = 'rsa_keys/private'

publ = 'rsa_keys/key.pub'"""

serwer = Server()
serwer.connectWithMongo()
# serwer.getFromMongo()

serwer.connectWithClient()
serwer.listening()
# serwer.stopConnection()