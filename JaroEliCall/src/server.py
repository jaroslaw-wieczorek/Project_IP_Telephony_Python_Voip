import pyaudio
import socket
from threading import Thread
import os
import json
import time
from bson.json_util import dumps
from JaroEliCall.src.mongoOperations import MongoOperations

# class Server(Validator):
class Server:
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 15
    FACTOR = 2

    def __init__(self):
        # Validator.__init__(self, priv, publ)
        print("Inicjalizacja klasy Server")
        self.host = ''
        self.port = 50001
        self.size = 2048
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)
        self.mongo = MongoOperations()

    def connectWithClient(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.bind((self.host, self.port))
        except ConnectionRefusedError as err:
            print(err)
            self.s.close()

    def sendAnything(self):
        self.mongo.runMongo()
        self.collection = self.mongo.collection

        while 1:
            time.sleep(2)
            test = self.collection.find({"status": "online"}, {"login": 1, "_id": 0})
            test = dumps(test)
            print(test)
            if (test):
                for key, value in self.mongo.dict_ip_users.items():
                    self.s.sendto(test.encode("utf-8"), value)

    def find_port(self, ip_addr):
        print(ip_addr)
        for key, value in self.dict_ip_users.items():
            print("keys ", key)
            if (key == ip_addr):
                return value

    def who_call(self, addr):
        print("Kto dzwoni ?? ")
        print(addr)
        for key, value in self.dict_ip_users.items():
            print(key)
            print(value)
            if (addr == value[0]):
                print("Adres IP ", addr, " user: ", key)
                return key
            else:
                print("Brak usera")
                return 0

    def get_username_from_ip(self, ip):
        for key, value in self.dict_ip_users.items():
            if (value[0] == ip[0]):
                return key

    def listening(self):
        print("[*] Start listen")

        while 1:
            d, addr = self.s.recvfrom(self.size * 2)
            print("Otrzymalem: ", d, " od ", addr)
            print(self.mongo.dict_ip_users)
            data = d[0:1].decode("utf-8")
            if (data[0:1] == "d"):

                communicate = d.decode("utf-8")
                print("Komunikat: ", communicate[7:12])
                print(communicate)
                if (communicate[2:7] == "LOGIN"):
                    print("Otrzymano LOGIN")
                    ans = self.mongo.checkWithMongo(communicate, addr)
                    if (ans == 1):
                        print('Wysylanie 200')
                        self.s.sendto(("200 OK").encode("utf-8"), addr)
                        print('Wysłano 200')

                    elif (ans == 0):
                        print('Wysylanie 406')
                        self.s.sendto(("406 NOT ACCEPTABLE").encode("utf-8"), addr)
                        print('Wyslano 406')

                elif (communicate[2:8] == "LOGOUT"):
                    print("Otrzymano LOGOUT")
                    ans = self.mongo.logoutUser(addr)
                    print("Odp na wylogowanie: ", ans)
                    if (ans == 1):
                        print('Wysylanie 200')
                        self.s.sendto(("200 OK").encode("utf-8"), addr)
                        print('Wysłano 200')

                    elif (ans == 0):
                        print('Wysylanie 401')
                        self.s.sendto(("401 UNAUTHORIZED").encode("utf-8"), addr)
                        print('Wyslano 401')


                elif (communicate[2:5] == "GET"):
                    print("Otrzymano GET")
                    self.mongo.getFromMongo()
                    print("Wysylanie userow")
                    self.s.sendto(("202" + json.dumps(self.mongo.users)).encode("utf-8"), addr)
                    print("Wyslano userow")

                elif (communicate[2:8] == "INVITE"):
                    frames = (communicate.split())
                    available = self.mongo.checkAvailibility(frames[2])
                    data_ip = self.find_port(frames[2])
                    if (available):
                        self.s.sendto(("200 OK ").encode("utf-8"), (addr))
                        self.s.sendto(("d INVITE EKaczmarek").encode("utf-8"), (data_ip))
                    else:
                        self.s.sendto(("460 NOT ACCEPTABLE").encode("utf-8"), (addr))
                elif (communicate[6:12] == "CREATE"):
                    frames = (communicate.split())
                    print("Tworzenie usera:", frames[4])
                    ans = self.mongo.find_in_mongo(frames[4])
                    print(addr)
                    if (ans == 1):
                        self.mongo.create_user(frames[4], frames[3], frames[5])
                        self.s.sendto(("201 CREATED").encode("utf-8"), addr)
                    elif (ans == 0):
                        self.s.sendto(("406 NOT ACCEPTABLE").encode("utf-8"), addr)
            elif (data[0:1] == "s"):
                print("Dzwiek: ")
                self.stream.write(d[2:])

        print("[*] Stop listen")

    def stopConnection(self):
        self.stream.stop_stream()
        self.stream.close()
        self.s.logoutAll()
        self.s.close()

        # p.close()


serwer = Server()
serwer.connectWithClient()
thread = Thread(target=serwer.listening, args=[])
thread.start()
thread_send = Thread(target=serwer.sendAnything, args=[])
thread_send.start()

