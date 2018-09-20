import os
import sys
import json
import socket
import pyaudio
from PyQt5 import QtCore
from threading import Event
import string

lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)
print(lib_path)

from JaroEliCall.src.test2 import ServerThread
from JaroEliCall.src.test2 import ClientThread
from threading import Thread
import random

# Server computer IP

#IP_server = '192.168.43.130'
IP_server = '127.0.0.1'
#IP_server = '192.168.43.70'
#IP_server = '192.168.0.4'

PORT_server = 50001


class Client(QtCore.QObject):
    # Signal to make calls
    makeCallSignal = QtCore.pyqtSignal(bool, str)

    # Signal to received calls
    getCallSignal = QtCore.pyqtSignal(bool, str)
    # WILL BE EXTEND ON AVATAR
    getMessage = QtCore.pyqtSignal(bool)
    callSignal = QtCore.pyqtSignal(bool, str, list)
    changedUsersStatusSignal = QtCore.pyqtSignal(bool, list)
    endCallResponse = QtCore.pyqtSignal(bool, str)

    registerMessage = QtCore.pyqtSignal(bool)

    activateAccountMessage = QtCore.pyqtSignal(bool, int)

    changedPasswordMessage = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(Client, self).__init__()
        print("Inicjalizacja klasy Client")

        global IP_server
        global PORT_server

        # Copy ip and port to class variables

        self.serverIP = IP_server
        self.serverPORT = PORT_server
        self.size = 2048
        self.last_list_users = []

        self.received = dict()
        self.connectToSerwer()
        self.username = None

    def connectToSerwer(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.connect((self.serverIP, self.serverPORT))
        except Exception as err:
            print("<!> Client Error in connectToServer:\n\t", err)
            self.socket.close()

    def sendMessage(self, data):
        try:
            self.socket.sendto(data, (self.serverIP, self.serverPORT))
            print("Wysłano ", data)
        except Exception as err:
            print("<!> Client Error in sendMessage:\n\t", err)

    def end_connection(self, person):
        payload = {"type": "d",
                   "description": "OK CLOSE CONNECTION",
                   "answer_to": "CONN_END",
                   "with_who": person}
        self.sendMessage(payload)

    def listeningServer(self):
        print("<*> Client info: run listeningServer")
        while True:
            print("<*> Client info: Listen now")
            try:
                packet, address = self.socket.recvfrom(self.size)
                data = packet.decode("utf-8")
                self.received = json.loads(data)
                print("CLIENT RECEIVED:", self.received)
                print(type(self.received))
                print("<*> Client info: Get response from server ", self.received)
                if self.received["type"] == "d":
                    self.react_on_communicate()
            except Exception as err:
                print("<!> Client Error in listeningServer:\n\t", err)

    def react_on_communicate(self):
        if (self.received["status"] == 200 and
                    self.received["answer_to"] == "LOGIN"):

            print("<*> Client info: React on comunicate: 200")
            # TO DO
            # self.my_login = self.received["login"]

            self.received = "200 LOGIN"
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 403 and
                      self.received["answer_to"] == "LOGIN" and
                      self.received["description"] == "NOT ACCEPTABLE"):

            self.received = "403 NOT ACCEPTABLE"
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 405 and
                      self.received["answer_to"] == "LOGIN" and
                      self.received["description"] == "NOT ACCEPTABLE"):

            self.received = "200 ACTIVATION OK"
            self.getMessage.emit(True)
            self.activateAccountMessage.emit(True, 200)

        elif (self.received["status"] == 200 and
                      self.received["answer_to"] == "CHANGE" and
                      self.received["description"] == "CHANGED"):

            print("Zmieniono hasło")
            self.received = "200 CHANGED"
            self.changedPasswordMessage.emit(True)
            self.getMessage.emit(True)

        elif (self.received["status"] == 409 and
                      self.received["answer_to"] == "LOGIN" and
                      self.received["description"] == "NOT ACCEPTABLE"):

            print("W polu hasło należy podać kod aktywacyjny")
            self.received = "409 NOT ACCEPTABLE"
            self.getMessage.emit(True)

        elif (self.received["status"] == 406 and
                      self.received["answer_to"] == "CHANGE" and
                      self.received["description"] == "CHANGED"):

            self.received = "406 NOT CHANGED"
            print("Nie zmieniono hasła")
            self.changedPasswordMessage.emit(False)
            self.getMessage.emit(True)


        elif (self.received["status"] == 203 and
                      self.received["answer_to"] == "AUTOMATIC_USERS_UPDATE"):
            # print("!!!! DOSTALEM UPDATE")
            if self.last_list_users != []:
                self.changedUsersStatusSignal.emit(True,
                                                   self.received["USERS"])


        elif self.received["status"] == 202:
            data = self.received["users"]
            self.last_list_users = data
            # TU POTRZEBA POPRAWIĆ
            print("Client get data from server:", data)

            self.status = "202 USERS"
            self.users = data
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 200 and
                      self.received["answer_to"] == "INVITE" and
                      self.received["description"] == "OK"):

            self.params = []
            self.status = "200 INVITE"
            self.getMessage.emit(True)
            for i in self.received['IP']:
                print(i)
                self.params.append(i)

        elif (self.received["status"] == 406 and
                      self.received["answer_to"] == "INVITE" and
                      self.received["description"] == "REJECTED"):

            self.status = "406 REJECTED"
            self.callSignal.emit(False, self.received["from_who"], [])

        elif (self.received["status"] == 402 and
                      self.received["answer_to"] == "LOGIN" and
                      self.received["description"] == "NOT ACCEPTABLE"):

            self.status = "402 NOT ACCEPTABLE"
            self.getMessage.emit(True)
            self.activateAccountMessage.emit(True, 402)


        elif (self.received["status"] == 200 and
                      self.received["answer_to"] == "ACTIVATE" and
                      self.received["description"] == "OK"):

            self.received = "200 ACTIVATION OK"
            self.getMessage.emit(True)
            self.activateAccountMessage.emit(True, 200)

        elif (self.received["status"] == 200 and
                      self.received["answer_to"] == "INVITE" and
                      self.received["description"] == "ANSWERED"):

            user_name = self.received["from_who"]
            user_name_ip = self.received["from_who_ip"]
            self.callSignal.emit(True, user_name, user_name_ip)

            self.status = "200 INVITE"
            print(user_name + " " + str(user_name_ip))
            # I EMIT SIGNAL getCall BECAUSE SOMEONE CALL TO ME
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

            self.voice(user_name_ip, 9999, 9998)

        elif (self.received["status"] == 406 and
                      self.received["answer_to"] == "INVITE"):

            self.status = "406 INVITE"
            print("406 INVITE")
            self.getMessage.emit(True)
            print("Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 200 and
                      self.received["answer_to"] == "NOTHING"):

            # save name and ip of person who is calling
            self.name_who = self.received["from_who"]
            self.from_who_ip = self.received["from_who_ip"]

            print("Dzwoni ", str(self.received["from_who"]))
            self.getCallSignal.emit(True, self.name_who)
            self.getMessage.emit(True)
            self.status = "200 INVITE"
            print("Client : info: makeCallSignal signal was emited with True")

        elif (self.received["status"] == 200 and
                      self.received["description"] == "END" and
                      self.received["answer_to"] == "CONN_END"):

            print("<*> Client info: Get status: %s" % self.received)
            self.getMessage.emit(True)
            self.endCallResponse.emit(True, self.received["from_who"])
            self.status = "200 END"
            print("<*> Client info: getMessage signal was emited with True")

            self.thread2.stopped.set()
            self.end_send_voice()

            self.thread1.stopped.set()
            self.end_receiving_sound()

        elif (self.received["status"] == 200 and
              self.received["description"] == "OK CLOSE CONNECTION"):
            print("<*> Client info: Get status: %s" % self.received)
            self.thread2.stopped.set()
            self.end_receiving_sound()

        elif (self.received["status"] == 406 and
              self.received["answer_to"] == "LOGIN"):
            self.received = "406 LOGIN"
            print("<*> Client info: Get status: %s" % self.received)
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 406 and
              self.received["answer_to"] == "REGISTER"):

            self.received = "406 CREATE"
            print("<*> Client info: Get status: %s" % (self.received))
            self.registerMessage.emit(False)
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 201 and 
              self.received["answer_to"] == "CREATE"):

            self.received = "201 CREATE"
            print("<*> Client info: Get status: %s" % self.received)
            self.registerMessage.emit(True)
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif self.received["status"] == 401:
            print("<*> Client info: Get status: %s " %  self.received)
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

        elif (self.received["status"] == 200 and
                      self.received["answer_to"] == "LOGOUT"):

            print("<*> Client info: Get status: %s" % self.received)
            self.getMessage.emit(True)
            print("<*> Client info: getMessage signal was emited with True")

    def login(self, login, password):
        payload = {"type": "d",
                   "description": "LOGIN",
                   "login": login,
                   "password": password}

        self.who_signed = login

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)
        self.username = login

    def logout(self):
        payload = {"type": "d",
                   "description": "LOGOUT"}

        data = json.dumps(payload).encode("utf-8")
        self.sendMessage(data)

    def get_avatar(self, user_name):
        avatar_name = ''
        for i in self.last_list_users:
            if i['login'] == user_name:
                avatar_name = i['avatar']
        print("get  avatar")
        print(self.last_list_users)
        print("user_name ", user_name)
        return avatar_name

    def reject_connection(self, from_who):
        payload = {"type": "d",
                   "description": "NOTHING",
                   "status": 406,
                   "from_who": from_who}

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)

    def answer_call(self, from_who):
        payload = {"type": "d",
                   "description": "NOTHING",
                   "status": 200,
                   "from_who": from_who}

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)

    def send_end_connection(self, from_who):
        payload = {"type": "d",
                   "description": "END",
                   "status": 200,
                   "from_who": from_who}
        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)

    def voice(self, user_name_ip, port_serwer, port_client):
        print("<*> Client info: Voice")
        self.threads = []

        # Create new threads
        # Run need port_serwer
        self.thread1 = ServerThread(1, "Server-Thread", 1)
        # Run need user_name_ip, port_client
        self.thread2 = ClientThread(2, "Client-Thread", 2)

        # Start new Threads
        self.thread1.setup(port_serwer)
        self.thread1.start()

        self.thread2.setup(user_name_ip, port_client)
        self.thread2.start()
        print("<*> Client info: threads started")

        # Add threads to thread list
        self.threads.append(self.thread1)
        self.threads.append(self.thread2)
        print("<*> Client info: Threads append to self.threads")

    def sendingVoice(self):
        if (self.user_name_ip != ''):
            print("<*> Client info: Someone is calling to me from:",
                  self.user_name_ip)

            print("<*> Client info: Start recording")
            self.voice(self.user_name_ip, 9998, 9999)

            print("<*> Client info: Stop recording")
        self.user_name_ip = ''

    def end_send_voice(self):
        self.thread2.close_clientSocket()

    def end_receiving_sound(self):
        self.thread1.close_serverSocket()

    def closeConnection(self):
        self.logout()
        self.socket.close()
