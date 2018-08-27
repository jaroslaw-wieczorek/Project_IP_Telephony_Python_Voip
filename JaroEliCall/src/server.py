import os
import re
import sys
import json
import time
import string
import random
import socket
import pyaudio
import smtplib
from threading import Thread


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

    def createActivationCode(self, length):
        ''.join(random.sample(string.ascii_letters +
                              string.digits +
                              string.punctuation, length))

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
                   "USERS": users }

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
        try:
            self.s.sendto(json.dumps(payload).encode("utf-8"), addr)
            print("Server : Sended: " + str(payload) + " to " + str(addr))
        except Exception as err:
          print(err.message)

    def log_in(self, login, password, addr):
        # print("Server log_in: get LOGIN")
        is_login_ok = self.mongo.checkWithMongo(login, password, addr)

        activated = self.mongo.check_is_account_activated(login)

        login_exists = self.mongo.check_if_login_exists(login)

        if login_exists:
            if activated:
                if is_login_ok:
                    self.send_login_200(addr)
                else:
                    is_password_equals_activation_code = self.mongo.check_login_code(login, password)
                    if is_password_equals_activation_code:
                        self.send_login_405(addr)
                    else:
                        self.send_login_409(addr)
            else:
                is_login_code_ok = self.mongo.check_login_code(login, password)
                if is_login_code_ok:
                    self.send_activate_200(addr)
                    self.mongo.update_mongo_activate(login)
                else:
                    self.send_login_403(addr)
        else:
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

    def send_login_409(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 409,
                   "answer_to": "LOGIN"}

        self.sending(addr, payload)

    def send_login_405(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 405,
                   "answer_to": "LOGIN"}

        self.sending(addr, payload)

    def send_activate_200(self, addr):
        payload = {"type": "d",
                   "description": "OK",
                   "status": 200,
                   "answer_to": "ACTIVATE"}

        self.sending(addr, payload)

    def send_login_402(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 402,
                   "answer_to": "LOGIN"}

        self.sending(addr, payload)

    def send_login_403(self, addr):
        payload = {"type": "d",
                   "description": "NOT ACCEPTABLE",
                   "status": 403,
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

        busy = self.is_recipient_has_conversation(where_name)

        if available and busy is False:

            where_ip = self.find_address(where_name)
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

    def is_recipient_has_conversation(self, who):
        ans = False
        for key, value in self.converstation_dictionary.items():
            print("key ", key)
            print("value ", value)
            if key == who or value == who:
                ans = True
        print("ans ", ans)
        return ans


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
        mongo = MongoOperations()
        email_exists = mongo.check_if_email_exists(communicate["EMAIL"])

        # print("Tworzenie usera:", communicate["NICKNAME"])
        ans = self.mongo.check_if_login_unique(communicate["NICKNAME"])
        # print(addr)
        if ans and email_exists is False:
            self.mongo.create_user(communicate["NICKNAME"],
                                   communicate["EMAIL"])

            self.send_created_200(addr)
        elif ans is False or email_exists is True:
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

                if str(received["type"]) == "d":
                    # print("Komunikat: ", (received["description"]))
                    if received["description"] == "LOGIN":
                        self.log_in(received["login"],
                                    received["password"], addr)
                    elif received["description"] == "LOGOUT":
                        self.log_out(addr)
                        # usuniecie z listy klientow z ktorymi jest polaczenie
                    elif received["description"] == "GET":
                        self.users_from_mongo(addr)
                    elif received["description"] == "INVITE":
                        recipient = received["call_to"]
                        # print("recipient ", recipient)
                        self.invite_person(recipient, addr)
                    elif received["description"] == "CREATE":
                        self.create_in_database(received, addr)
                    elif received["description"] == "LOGOUT":
                        self.log_out(addr)
                    elif received["description"] == "NOTHING":
                        # print("informacja od recipient
                        # czy odebral lub odrzucil")
                        self.send_info_to_caller(received["status"],
                                                 addr,
                                                 received["from_who"])

                    elif received["description"] == "END":
                        self.check_caller(received["from_who"])

                    elif received["description"] == "OK CLOSE CONNECTION":
                        self.send_ok_end_connection(received["with_Who"])

                    elif received["description"] == "CHANGE":
                        print("[***] Server!! received[\"AVATAR\"] with: ", received["AVATAR"])
                        self.change_user_password(received["NICKNAME"], received["PASSWORD"], received["AVATAR"], addr)

            except ConnectionResetError as err:
                print("Połączenie przerwane przez klienta\n")
        # print("[*] Stop listen")

    def send_ok_end_connection(self, with_who):
        payload = {"type": "d",
                   "description": "OK CLOSE CONNECTION",
                   "status": 200,
                   "from_who": with_who,
                   "answer_to": "CONN_END"}

        ip = self.find_address(with_who)
        self.end_of_conn = payload
        self.sending(ip, payload)

    def check_caller(self, from_who):
        caller = self.converstation_dictionary[from_who]
        print(str(from_who) + " rozmawia z " + str(caller))
        self.send_end_connection_person(caller, from_who)

        del self.converstation_dictionary[caller]
        del self.converstation_dictionary[from_who]

    def change_user_password(self, login, password_hash, avatar, addr):
        changed = self.mongo.change_password_mongo(login, password_hash, avatar)
        if changed:
            self.send_changed_200(addr)
        else:
            # login podany nie istnieje w bazie
            self.send_changed_406(addr)

    def send_changed_200(self, addr):
        payload = {"type": "d",
                   "description": "CHANGED",
                   "status": 200,
                   "answer_to": "CHANGE"}

        self.sending(addr, payload)

    def send_changed_406(self, addr):
        payload = {"type": "d",
                   "description": "CHANGED",
                   "status": 406,
                   "answer_to": "CHANGE"}

        self.sending(addr, payload)

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
