import pyaudio
import socket
import time
from pymongo import MongoClient
# from validation import Validator
import os
import json
from sys import platform


# class Server(Validator):
class Server:
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    WIDTH = 1
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 15
    FACTOR = 2

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


    def listening(self):
        print("[*] Start listen")

        while 1:
            d, addr = self.s.recvfrom(self.size*2)
            print("Otrzymalem: ", d, " od ", addr)
            data = d[0:1].decode("utf-8")
            print(data)
            if (data[0:1] == "d"):
                communicate = d.decode("utf-8")
                print(communicate)
                if(communicate[2:7]=="LOGIN"):
                    print("Otrzymano LOGIN")
                    ans = self.checkWithMongo(communicate)
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
                    print("Najpierw dzwonie tylko do serwera")

            elif (data[0:1]=="s"):
                print("Dzwiek: ")
                #self.stream.read(d[3:])
                self.stream.write(d[2:])


        print("[*] Stop listen")

    def stopConnection(self):
        self.stream.stop_stream()
        self.stream.close()

        self.s.close()

        # p.close()

    def checkWithMongo(self, data):
        print("Sprawdzenie z mongo")
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']

        print(data)
        frames = (data.split())

        try:
            answer = (collection.find({"login": frames[3], "password": frames[4]}).count()) == 1

            if (answer):
                collection.update({"login": frames[3], "password": frames[4]}, {"$set": {"status": "available"}})
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