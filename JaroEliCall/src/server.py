import os
import re
import sys
import json
import time
import string
import random
import socket
import pyaudio

from threading import Thread
from bson.json_util import dumps

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

from mongoOperations import MongoOperations

# print(lib_path)
# class Server(Validator):

# IP to listen
Listen_IP = '0.0.0.0'


class Server:

    def __init__(self):
        # print("Inicjalizacja klasy Server")
        global Listen_IP
        self.host = Listen_IP
        self.port = 50001
        self.size = 2048

        self.mongo = MongoOperations()
        self.converstation_dictionary = {}

        self.end_of_conn = ''


    def connectWithClient(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.bind((self.host, self.port))

        except ConnectionRefusedError as err:
            # print(err)
            self.s.close()

    def send_update_users(self):
        while True:
            time.sleep(5)
            # # print(" [*][*] BEGINNING UPDATE USERS METHOD [*][*] ")
            self.mongo.getFromMongo()
            # # print("Uzytkownicy: " + str(self.mongo.users))
            self.send_to_all_users(self.mongo.users)
            # # print(" [*][*] END UPDATE USERS METHOD [*][*] ")

    def send_to_all_users(self, users):
        payload = {"type": "d",
                   "status": 203,
                   "description": "USERS_UPDATE",
                   "answer_to":  "AUTOMATIC_USERS_UPDATE",
                   "USERS": users}

        if(self.end_of_conn) != '':
            payload = self.end_of_conn
        # print(payload)
        for key, value in self.mongo.dict_ip_users.items():
            # print(key, " ", value)
            self.sending(value, payload)
        self.end_of_conn = ''

    def find_address(self, login):
        # print(login)
        for key, value in self.mongo.dict_ip_users.items():
            if (key == login):
                # print(key)
                return value

    def get_username_from_ip(self, ip):
        # print("Server w funkcji get_username_from_ip")
        ans = "brak usera"
        for key, value in self.mongo.dict_ip_users.items():
            # print(ip)
            # print(key, '', value)
            if (value[0] == ip[0] and value[1] == ip[1]):
                ans = key
        return ans

    def sending(self, addr, payload):
        self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
        print("Server : Sended: " + str(payload) + " to " + str(addr))

    def log_in(self, login, password, addr):
        # print("Server log_in: get LOGIN")
        is_login_ok = self.mongo.checkWithMongo(login, password, addr)
        if (is_login_ok):
            self.send_login_200(addr)
        elif (is_login_ok == 0):
            self.send_login_406(addr)

    def send_login_200(self, addr):
        payload = {"type": "d",
                   "description": "OK",
                   "status": 200,
                   "answer_to": "LOGIN"}

        self.sending(addr, payload)

    def send_login_406(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 406,
                   "answer_to": "LOGIN"}

        self.sending(addr, payload)

    def log_out(self, addr):
        # print("Server log_out get: LOGOUT")
        ans = self.mongo.logoutUser(addr)
        # print("Odp na wylogowanie: ", ans)
        """if (ans == 1):
            self.send_logout_200(addr)
        elif (ans == 0):
            self.send_logout_406(addr)"""

    def send_logout_200(self, addr):
        payload = {"type": "d",
                   "description": "OK",
                   "status": 200,
                   "answer_to": "LOGOUT"}

        self.sending(addr, payload)

    def send_logout_406(self, addr):
        payload = {"type": "d",
                   "description": "UNAUTHORIZED",
                   "status": 401,
                   "answer_to": "LOGOUT"}

        self.sending(addr, payload)

    def users_from_mongo(self, addr):
        self.mongo.getFromMongo()
        self.send_get_202(addr)

    def send_get_202(self, addr):
        payload = {"type": "d",
                   "users": self.mongo.users,
                   "status": 202,
                   "answer_to": "GET"}

        self.sending(addr, payload)

    # connection_receiver login osoby do ktorej chce zadzwonic
    def invite_person(self, where_name, who_ip):
        available = self.mongo.checkAvailibility(where_name)

        if(available):
            where_ip = self.find_address(where_name)
            # print("Moje argumenty " + str(who_ip) + " dzwoni do " + str(where_name) + " o IP: " + str(where_ip))
            who_name = self.get_username_from_ip(who_ip)

            if(who_name != "brak usera"):

                # informacja do odbiorcy o tym że ktoś dzwoni
                self.send_inf_connection_is_comming_200_to_recipient(where_ip,
                                                                     who_name,
                                                                     who_ip)

                # informacja do strony ktora dzwoni o
                # danych osoby do ktorej dzwoni
                self.send_invite_200_to_caller(where_ip, who_ip)

            else:
                self.send_invite_406(who_ip)
        else:
            self.send_invite_406(who_ip)

    def send_inf_connection_is_comming_200_to_recipient(self, where_ip,
                                                        who_name, who_ip):
        payload = {"type": "d",
                   "description": "INVITE",
                   "answer_to": "NOTHING",
                   "status": 200,
                   "from_who": who_name,
                   "from_who_ip": who_ip}

        self.sending(where_ip, payload)

    def send_invite_200_to_caller(self, addr, caller):

        payload = {"type": "d",
                   "description": "OK",
                   "status": 200,
                   "answer_to": "INVITE",
                   "IP": addr}

        self.sending(caller, payload)

    def send_invite_406(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 406,
                   "answer_to": "INVITE"}

        self.sending(addr, payload)

    def create_in_database(self, communicate, addr):
        # print("Tworzenie usera:", communicate["NICKNAME"])
        ans = self.mongo.find_in_mongo(communicate["NICKNAME"])
        # print(addr)
        if (ans == 1):
            self.mongo.create_user(communicate["NICKNAME"],
                                   communicate["EMAIL"],
                                   communicate["PASSWORD"])

            self.send_created_200(addr)
        elif (ans == 0):
            self.send_created_406(addr)

    def send_created_200(self, addr):
        payload = {"type": "d",
                   "description": "CREATED",
                   "status": 201,
                   "answer_to": "CREATE"}

        self.sending(addr, payload)

    def send_created_406(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 406,
                   "answer_to": "REGISTER"}

        self.sending(addr, payload)

    def send_info_to_caller(self, status,
                            who_ans_or_rejected_ip,
                            addr_nickname):
        who_ansewer_on_con = self.get_username_from_ip(who_ans_or_rejected_ip)
        addr = self.find_address(addr_nickname)
        # print("who_ansewer_on_con ", who_ansewer_on_con)
        if(status == 406):
            self.send_rejected_406(addr, who_ansewer_on_con)
        elif status == 200:

            self.converstation_dictionary[addr_nickname] = who_ansewer_on_con
            self.converstation_dictionary[who_ansewer_on_con] = addr_nickname
            print("converstation_dictionary" +
                  str(self.converstation_dictionary))
            self.send_answered_200(addr, who_ansewer_on_con)

    def send_rejected_406(self, addr, conn_with_who):
        payload = {"type": "d",
                   "description": "REJECTED",
                   "status": 406,
                   "answer_to": "INVITE",
                   "from_who": conn_with_who,
                   "from_who_ip": self.find_address(conn_with_who)}

        self.sending(addr, payload)

    def send_answered_200(self, addr, conn_with_who):
        payload = {"type": "d",
                   "description": "ANSWERED",
                   "status": 200,
                   "answer_to": "INVITE",
                   "from_who": conn_with_who,
                   "from_who_ip": self.find_address(conn_with_who)}

        self.sending(addr, payload)

    def listening(self):
        # print("[*] Start listen")
        while 1:
            # print("[*] Czekam na kolejna wiadomosc")
            try:
                d, addr = self.s.recvfrom(self.size * 2)
                print("Otrzymalem: ", d, " od ", addr)
                # print(self.mongo.dict_ip_users)
                data = d.decode("utf-8")
                received = json.loads(data)

                if (str(received["type"]) == "d"):
                    # print("Komunikat: ", (received["description"]))
                    if (received["description"] == "LOGIN"):
                        self.log_in(received["login"],
                                    received["password"], addr)
                    elif (received["description"] == "LOGOUT"):
                        self.log_out(addr)
                        # usuniecie z listy klientow z ktorymi jest polaczenie
                    elif (received["description"] == "GET"):
                        self.users_from_mongo(addr)
                    elif (received["description"] == "INVITE"):
                        recipient = received["call_to"]
                        # print("recipient ", recipient)
                        self.invite_person(recipient, addr)
                    elif (received["description"] == "CREATE"):
                        self.create_in_database(received, addr)
                    elif (received["description"] == "LOGOUT"):
                        self.log_out(addr)
                    elif (received["description"] == "NOTHING"):
                        # print("informacja od recipient
                        # czy odebral lub odrzucil")
                        self.send_info_to_caller(received["status"],
                                                 addr,
                                                 received["from_who"])

                    elif received["description"] == "END":
                        self.check_caller(received["from_who"])

            except ConnectionResetError as err:
                print("Połączenie przerwane przez klienta\n", err.message)
        # print("[*] Stop listen")

    def check_caller(self, from_who):
        caller = self.converstation_dictionary[from_who]
        print(str(from_who) + " rozmawia z " + str(caller))
        self.send_end_connection_person(caller, from_who)
        self.converstation_dictionary[caller] = ''
        self.converstation_dictionary[from_who] = ''

    def send_end_connection_person(self, person, from_who):
        ip = self.find_address(person)
        payload = {"type": "d",
                   "description": "END",
                   "status": 200,
                   "from_who": from_who,
                   "answer_to": "CONN_END"}

        self.end_of_conn = payload
        self.sending(ip, payload)

    def stopConnection(self):
        self.stream.stop_stream()
        self.stream.close()
        self.s.logoutAll()
        self.s.close()


serwer = Server()
serwer.connectWithClient()
thread = Thread(target=serwer.listening, args=[])
thread.start()

thread2 = Thread(target=serwer.send_update_users, args=[])
thread2.start()
