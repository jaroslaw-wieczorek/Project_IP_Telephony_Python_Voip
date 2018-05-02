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


    def __init__(self, priv, publ):

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

        while True:
        #for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            try:
                data, addr = self.s.recvfrom(self.size)
                self.host = addr[0]
                self.port = addr[1]
                print(self.host)
                print(self.port)



                if data:
                    self.stream.write(data)  # Stream the recieved audio data
                    print(type(data), data)
                    try:
                        data = data.decode("utf-8")
                        if (data[0:5] == "LOGIN"):
                            print("Otrzymano LOGIN")
                            ans = self.checkWithMongo(data)
                            if (ans == 1):
                                print('Wysylanie 200')
                                self.sendM("200 OK")
                                print('Wysłano 200')


                            elif (ans == 0):
                                print('Wysylanie 406')
                                self.sendM("406 NOT ACCEPTABLE")
                                print('Wyslano 406')

                        elif(data[0:3] =="GET"):
                            print("Otrzymano GET")
                            self.getFromMongo()
                            print("Wysylanie userow")
                            self.sendM("202" + json.dumps(self.users))
                            print("Wyslano userow")
                            break

                    except UnicodeDecodeError:
                        print("Bład dekodowania")

            except ConnectionRefusedError as err:
                print(err)
                print("Bład połączenia")
                break

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



priv = 'rsa_keys/private'

publ = 'rsa_keys/key.pub'

serwer = Server(priv, publ)
serwer.connectWithMongo()
serwer.getFromMongo()

serwer.connectWithClient()
serwer.listening()
#serwer.stopConnection()