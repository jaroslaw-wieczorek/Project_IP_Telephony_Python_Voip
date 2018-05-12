import pyaudio
import socket
import time 
from pymongo import MongoClient
#from validation import Validator
import os
import json

#class Server(Validator):
class Server:

    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    WIDTH = 1
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 15
    FACTOR = 2


    def __init__(self):

        #Validator.__init__(self, priv, publ)
        print("Inicjalizacja klasy Server")
        
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=self.CHUNK)

    def connectWithMongo(self):
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


    def sendM(self, message):
        self.s.connect((self.host, self.port))
        self.s.send(message.encode("utf-8"))


    def listening(self):
        print("[*] Start listen")

        while 1:
            data, addr = self.s.recvfrom(self.size)
            print(addr)
            print("Otrzymalem: ", data)
            self.s.sendto(("Otrzymalem: ").encode("utf-8"), addr)

        print("[*] Stop listen")


    def stopConnection(self):
        self.stream.stop_stream()
        self.stream.close()

        self.s.close()

        #p.close()


    def checkWithMongo(self, data):
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']

        print(data)
        frames = (data.split())

        try:
            answer = (collection.find({"login": frames[2], "password": frames[3]}).count()) == 1

            if (answer):
                collection.update({"login": frames[2], "password": frames[3]}, {"$set":{"status":"available"}})
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
#serwer.connectWithMongo()
#serwer.getFromMongo()

serwer.connectWithClient()
serwer.listening()
#serwer.stopConnection()