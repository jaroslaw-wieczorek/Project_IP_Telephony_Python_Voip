
import os
import sys

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

import pyaudio
import socket
import json
import time
import threading

import PyQt5

from PyQt5 import QtCore

from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSignal

class Client(QtCore.QObject):

    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 2
    FACTOR = 2


    getMessage = QtCore.pyqtSignal(bool)

    getCall = QtCore.pyqtSignal(bool)

    def __init__(self, SERWER_IP, port):
        super(Client, self).__init__()
        print("Inicjalizacja klasy Client")
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

        self.received = None
        self.connectToSerwer(SERWER_IP, port)

        self.username = None


    def connectToSerwer(self, host, port):
        # ipadres serwera
        print("Laczenie z serwerem")
        self.host = host
        self.port = port
        self.size = 2048

        try:

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.connect((self.host, self.port))
            print("Polaczono z serwerem")

        except ConnectionRefusedError as err:

            print(err)
            self.socket.close()


    def sendMessage(self, data):
        try:
            self.socket.sendto(data, (self.host, self.port))
            print("Wysłano ", data)

        except ConnectionRefusedError as err:
            print(err)


    def sendMessage_another_client(self, data, host, port):
        try:
            self.socket.connect((host, port))
            self.socket.sendto(data, (host, port))
            print("Wysłano ", data)
        except ConnectionRefusedError as err:
            print(err)


    def listeningServer(self):
        print("\tClinet : info >> run listeningServer")
        while True:
            print("\tClinet : info >> Listen now")

            packet, address = self.socket.recvfrom(self.size)
            data = packet.decode("utf-8")
            self.received = json.loads(data)

            print("\tClinet : info >> Get response from server ", self.received)

            if str(self.received["type"]) == "d":
                self.react_on_communicate()




    def react_on_communicate(self):
        if self.received["status"] == 200 and self.received["answer_to"] == "LOGIN":
            print("Clinet : info >> React on comunicate: 200")
            self.received = "200 LOGIN"
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")
                        #self.toThread.lock.release()
            # toThread.self.received = ("200 LOGIN")

        # below to change on signals
        elif self.received["status"] == 202:
            data = self.received["users"]
            # TU POTRZEBA POPRAWIĆ
            print("Client get data from server:", data)

            self.received = "202 USERS"
            self.users = data
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")

        elif self.received["status"] == 200 and self.received["answer_to"] == "INVITE":
            for i in self.received['IP']:
                print(i)
            self.params = self.received['IP'][0]
            print("200 INVITE ")
            self.received = "200 INVITE"
            self.getCall.emit(True)
            print("Clinet : info >> getCall signal was emited with True")

        elif self.received["status"] == 406 and self.received["answer_to"] == "INVITE":
            self.received = "406 INVITE"
            print("406 INVITE")
            self.getCall.emit(True)
            print("Clinet : info >> getCall signal was emited with True")


        elif self.received["status"] == 200 and self.received["answer_to"] == "NOTHING":
            # toThread.self.received = ("200 NOTHING " + str(self.received["from_who"]))
            print("200 INVITE ", self.received["from_who"])
            print("Dzwoni ", str(self.received["from_who"]))
            self.getCall.emit(True)
            print("Clinet : info >> getCall signal was emited with True")




        elif self.received["status"] == 406 and self.received["answer_to"] == "LOGIN":
            self.received = "406 LOGIN"
            print("406")
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")

        elif self.received["status"] == 406 and self.received["answer_to"] == "CREATE":
            # toThread.self.received = ("406 NOT_CREATED")
            print("406")
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")

        elif self.received["status"] == 201 and self.received["answer_to"] == "CREATE":
            #toThread.self.received = ("201 CREATED")
            print("201 CREATE ")
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")

        elif self.received["status"] == 401:
            print("401")
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")

        elif self.received["status"] == 200 and self.received["answer_to"] == "LOGOUT":
            #toThread.self.received = ("200 LOGOUT")
            print("200")
            self.getMessage.emit(True)
            print("Clinet : info >> getMessage signal was emited with True")


    def login(self, login, password):
        payload = {"type": "d", "description": "LOGIN", "login": login, "password": password}
        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)
        self.username = login



    def sendingVoice(self):
        print("\tClinet : info >> Start recording")

        while True:
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

        print("\tClinet : info >> Stop recording")


    def closeConnection(self):
        self.stream.stop_stream()
        self.stream.close()
        self.socket.close()


    def logout(self):
        # TO DO:
        print("\tClinet : info >> Logout")
