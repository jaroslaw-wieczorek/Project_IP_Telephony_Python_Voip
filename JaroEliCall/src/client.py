import os
import sys
import json
import socket
import pyaudio
from threading import Thread
from PyQt5 import QtCore


lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)
print(lib_path)

from JaroEliCall.src.test2 import ServerThread
from JaroEliCall.src.test2 import ClientThread


# Local computer IP
IP_local = '192.168.0.101'

# Server computer IP
IP_server = '192.168.0.101'
PORT_server = 50001

# Remote computer IP
IP_remote = '192.168.0.104'


class Client(QtCore.QObject):
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 2
    FACTOR = 2

    # Signal to make calls
    makeCallSignal = QtCore.pyqtSignal(bool, str)

    # Signal to received calls
    getCallSignal = QtCore.pyqtSignal(bool, str) #WILL BE EXTEND ON AVATAR

    getMessage = QtCore.pyqtSignal(bool)

    callSignal = QtCore.pyqtSignal(bool, str, list)


    def __init__(self):
        super(Client, self).__init__()
        print("Inicjalizacja klasy Client")

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

        global IP_server
        global PORT_server

        # Copy ip and port to class variables

        self.serverIP = IP_server
        self.serverPORT = PORT_server
        self.size = 2048

        self.received = None
        self.connectToSerwer()
        self.username = None


    def connectToSerwer(self):
        # ipadres serwera
        print("Laczenie z serwerem")

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.connect((self.serverIP, self.serverPORT))
            print("Polaczono z serwerem")

        except ConnectionRefusedError as err:
            print(err)
            self.socket.close()

    def sendMessage(self, data):
        try:
            self.socket.sendto(data, (self.serverIP, self.serverPORT))
            print("Wysłano ", data)
        except ConnectionRefusedError as err:
            print(err)


    def listeningServer(self):
        print("\tClient : info >> run listeningServer")
        while True:
            print("\tClient : info >> Listen now")

            packet, address = self.socket.recvfrom(self.size)
            data = packet.decode("utf-8")
            self.received = json.loads(data)

            print("\tClient : info >> Get response from server ", self.received)

            if str(self.received["type"]) == "d":
                self.react_on_communicate()


    def react_on_communicate(self):
        if self.received["status"] == 200 and self.received["answer_to"] == "LOGIN":
            print("Client : info >> React on comunicate: 200")
            self.received = "200 LOGIN"
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")
                        #self.toThread.lock.release()
        # toThread.self.received = ("200 LOGIN")
        # below to change on s ignals
        elif self.received["status"] == 202:
            data = self.received["users"]
            # TU POTRZEBA POPRAWIĆ
            print("Client get data from server:", data)

            self.status = "202 USERS"
            self.users = data
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

        elif self.received["status"] == 200 and self.received["answer_to"] == "INVITE" and self.received["description"] == "OK":
            self.params = []
            self.status = "200 INVITE"
            self.getMessage.emit(True)
            for i in self.received['IP']:
                print(i)
                self.params.append(i)

        elif self.received["status"] == 406 and self.received["answer_to"] == "INVITE" and self.received["description"] == "REJECTED":
            self.status = "406 REJECTED"
            self.callSignal.emit(False, self.received["from_who"], [])


        elif self.received["status"] == 200 and self.received["answer_to"] == "INVITE" and self.received["description"] == "ANSWERED":
            user_name = self.received["from_who"]
            user_name_ip = self.received["from_who_ip"]
            self.callSignal.emit(True, user_name, user_name_ip)

            self.status = "200 INVITE"
            print(user_name + " " + str(user_name_ip))
            # I EMIT SIGNAL getCall BECAUSE SOMEONE CALL TO ME
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

            self.voice(user_name_ip)

        elif self.received["status"] == 406 and self.received["answer_to"] == "INVITE":
            self.status = "406 INVITE"
            print("406 INVITE")
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

        elif self.received["status"] == 200 and self.received["answer_to"] == "NOTHING":

            user_name = str(self.received["from_who"])
            print("200 INVITE ", self.received["from_who"])
            print("Dzwoni ", str(self.received["from_who"]))
            self.user_name_ip = self.received["from_who_ip"]
            self.getCallSignal.emit(True, user_name)
            self.getMessage.emit(True)
            self.status = "200 INVITE"
            print("Client : info >> makeCallSignal signal was emited with True")


        elif self.received["status"] == 406 and self.received["answer_to"] == "LOGIN":
            self.received = "406 LOGIN"
            print("406")
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

        elif self.received["status"] == 406 and self.received["answer_to"] == "CREATE":
            print("406")
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

        elif self.received["status"] == 201 and self.received["answer_to"] == "CREATE":
            print("201 CREATE ")
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

        elif self.received["status"] == 401:
            print("401")
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")

        elif self.received["status"] == 200 and self.received["answer_to"] == "LOGOUT":
            print("200")
            self.getMessage.emit(True)
            print("Client : info >> getMessage signal was emited with True")


    def login(self, login, password):
        payload = {"type": "d", "description": "LOGIN",
                   "login": login, "password": password}

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)
        self.username = login


    def logout(self):
        payload = {"type": "d", "description": "LOGOUT"}
        data = json.dumps(payload).encode("utf-8")
        self.sendMessage(data)


    def reject_connection(self, from_who):
        payload = {"type": "d", "description": "NOTHING", "status": 406,
                   "from_who": from_who}
        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)

    def answer_call(self, from_who):
        payload = {"type": "d", "description": "NOTHING", "status": 200,
                   "from_who": from_who}
        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)


    def voice(self, user_name_ip):
        threads = []

        #global IP_remote
        # global IP_remote
        IP_remote = '192.168.0.104'
        # Create new threads
        thread1 = ServerThread(1, "Server-Thread", 1, 9998)
        thread2 = ClientThread(2, "Client-Thread", 2, user_name_ip, 9999)

        # Start new Threads
        thread1.start()
        thread2.start()

        # Add threads to thread list
        threads.append(thread1)
        threads.append(thread2)

        # Wait for all threads to complete
        for t in threads:
            t.join()

        print("Exiting Main Thread")


    def sendingVoice(self):

        if(self.user_name_ip != ''):
            print("Someone is calling to me - her/his ip is ", self.user_name_ip)
            print("\tClient : info >> Start recording")

            self.voice(self.user_name_ip)

            """while True:
                for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                    print("\t send:", i)

                    self.data = "s ".encode("utf-8") + self.stream.read(self.CHUNK)

                    if self.data:
                        # Write data to pyaudio stream
                        self.stream.write(self.data)  # Stream the recieved audio data

                        try:
                            self.socket.send(self.data)
                            print("< Client > Info: Send data", self.data)
                        except ConnectionRefusedError as err:
                            # TO DO throw this exception upper to managment
                            # for try reconnect
                            print(err)
                            break
            """

            print("\tClient : info >> Stop recording")
        self.user_name_ip = ''



    def closeSendingVoice(self):
        self.stream.stop_stream()
        self.stream.close()


    def closeConnection(self):
        self.logout()
        self.socket.close()
