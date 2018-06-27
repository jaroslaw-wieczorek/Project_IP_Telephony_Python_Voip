import os
import sys
import pyaudio
import socket
from threading import Thread
import json
import time
from bson.json_util import dumps
from mongoOperations import MongoOperations

#lib_path = os.path.abspath(os.path.join(__file__))
#sys.path.append(lib_path)


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
                    print("key: ", key)
                    print("value ", value)
                    self.users_from_mongo(value)


    def find_address(self, login):
        print(login)
        for key, value in self.mongo.dict_ip_users.items():
            print("keys ", key)
            if (key == login):
                print("Znaleziono ", value)
                print(key)
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

    def log_in(self, login, password, addr):
        print("Otrzymano LOGIN")
        is_login_ok = self.mongo.checkWithMongo(login, password, addr)
        if (is_login_ok):
            # {"type":"d", "description":"OK", "status":200}
            # {"type":"d", "description":"SEND", "status":202, "users":}
            print('Wysylanie 200')
            payload = {"type": "d", "description": "OK", "status": 200, "answer_to": "LOGIN" }
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            print('Wysłano 200')

        elif (is_login_ok == 0):
            print('Wysylanie 406')
            payload = {"type": "d","description": "NOT ACCEPTABLE", "status": 406, "answer_to": "LOGIN"}
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            print('Wyslano 406')

    def log_out(self, addr):
        print("Otrzymano LOGOUT")
        ans = self.mongo.logoutUser(addr)
        print("Odp na wylogowanie: ", ans)
        if (ans == 1):
            print('Wysylanie 200')
            payload = {"type": "d", "description": "OK", "status": 200, "answer_to": "LOGOUT"}
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            print('Wysłano 200')
        elif (ans == 0):
            print('Wysylanie 401')
            payload = {"type": "d", "description": "UNAUTHORIZED", "status": 401, "answer_to": "LOGOUT"}
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            # self.s.sendto(("401 UNAUTHORIZED").encode("utf-8"), addr)
            print('Wyslano 401')


    def users_from_mongo(self, addr):
        print("Otrzymano GET")
        self.mongo.getFromMongo()
        print("Uzytkownicy: " + str(self.mongo.users))
        payload = {"type" : "d", "users": self.mongo.users, "status": 202, "answer_to": "GET"}
        message = json.dumps(payload)
        self.s.sendto(message.encode("utf-8"), addr)
        print("Wyslano WIADOMOSC" + str(type(message)) + " " + str(message) + " do " + str(addr))

    def invite_person(self, connection_receiver, connection_caller_ip):
        # dostaję nazwe uzytkownika osoby do ktorej chce zadzwonic
        # musze ogarnac jaki jest jej port i adres ip

        available = self.mongo.checkAvailibility(connection_receiver)
        print("Dostepnosc osoby " + str(connection_receiver) + " " + str(available))

        if(available):
            receiver_ip = self.find_address(connection_receiver)
            print("dane ip osoby: ", receiver_ip)

            payload = {"type": "d","description": "OK", "status": 200, "answer_to": "INVITE", "IP": receiver_ip}
            self.s.sendto(json.dumps(payload).encode("utf-8"), connection_caller_ip)

            message = {"type": "d", "description": "INVITE", "status": 200, "from_who": connection_caller_ip}
            self.s.sendto(json.dumps(message).encode("utf-8"), receiver_ip)
            print(message)
        else:
            payload = {"type": "d", "description": "NOT ACCEPTABLE", "status": 406, "answer_to": "INVITE"}
            self.s.sendto(json.dumps(payload).encode("utf-8"), connection_caller_ip)
            print(payload)

    def create_in_database(self, communicate, addr):
        print("Tworzenie usera:", communicate["NICKNAME"])
        ans = self.mongo.find_in_mongo(communicate["NICKNAME"])
        print(addr)
        if (ans == 1):
            self.mongo.create_user(communicate["NICKNAME"], communicate["EMAIL"], communicate["PASSWORD"])
            payload = {"type": "d", "description": "CREATED", "status": 201, "answer_to": "CREATE"}
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            print("Wyslano ", payload)

        elif (ans == 0):
            payload = {"type": "d", "description": "NOT ACCEPTABLE", "status": 406, "answer_to": "REGISTER"}
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            print("Wyslano ", payload)


    def listening(self):
        print("[*] Start listen")
        while 1:
            """d, addr = self.s.recvfrom(self.size * 2)
            print("Otrzymalem: ", d, " od ", addr)
            print(self.mongo.dict_ip_users)
            data = d.decode("utf-8")
            print("DEKODOWANIE: " + data)"""
            print("Czekam na kolejna wiadomosc")
            try:
                d, addr = self.s.recvfrom(self.size * 2)
                print("Otrzymalem: ", d, " od ", addr)
                print(self.mongo.dict_ip_users)
                data = d.decode("utf-8")
                received = json.loads(data)
                print("DEKODOWANIE: " + str(received["type"]))
                print("TYP" + str(type(data)))

                #print("type: "+d["type"].decode("utf-8"))
                #if(data[0:1] == "d"):
                if (str(received["type"]) == "d"):
                    print("Komunikat: ", (received["description"]))
                    if (received["description"] == "LOGIN"):
                        self.log_in(received["login"], received["password"], addr)
                    elif (received["description"] == "LOGOUT"):
                        self.log_out(addr)
                        # usuniecie z listy klientow z ktorymi jest polaczenie
                    elif (received["description"] == "GET"):
                        self.users_from_mongo(addr)
                    elif (received["description"] == "INVITE"):
                        self.invite_person(received["call_to"], addr)
                    elif (received["description"] == "CREATE"):
                        self.create_in_database(received, addr)
                    elif (received["description"] == "LOGOUT"):
                        self.log_out(addr)
                #elif (data[0:1] == "s"):EK
                elif (str(received["type"]) == "s"):
                    print("Dzwiek: ")
                    self.stream.write(d[2:])
            except ConnectionResetError:
                print("Połączenie przerwane przez klienta")


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


"""thread_send = Thread(target=serwer.sendAnything, args=[])
thread_send.start()"""

