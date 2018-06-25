
import os
import sys


import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QApplication


lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)


lib_path2 = os.path.abspath(os.path.join(__file__, '..','..', '..'))
sys.path.append(lib_path2)

print(lib_path2)

import pyaudio
import socket
from JaroEliCall.src.actionsViews.Interaction_code import InteractionWidget
import threading
import json
from JaroEliCall.src.actionsViews.AdduserWidget_code import AddUserWidget
from threading import Thread




#class Client(Validator):
class Client:
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 15
    FACTOR = 2

    #def __init__(self, priv, publ):

    def __init__(self):
        print("Inicjalizacja klasy Client")

        """self.__private_key = priv
        self.__public_key = publ"""

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

    def connectToSerwer(self, host):
        # ipadres serwera
        print("Laczrenie z serwerem")
        self.host = host
        self.port = 50001
        self.size = 2048

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.connect((self.host, self.port))
            print("Polaczono z serwerem")



        except ConnectionRefusedError as err:
            print(err)
            self.s.close()

    def sendMessage(self, data):
        print("Wiadomosc do wyslania do serwera: ", self.host)
        try:
            self.s.sendto(data, (self.host, self.port))
            self.thread = Thread(target=self.listening, args=[])
            self.thread.start()
        except ConnectionRefusedError as err:
            print(err)


    def show_add_users(self):
        print("Do addUserWidget")
        self.users = AddUserWidget(self)
        print("Do load contacts")
<<<<<<< HEAD
        users.load_contracts()
        users.show()
     #   users.exec_()
=======

        payload = {"type": "d", "description": "GET"}
        data = json.dumps(payload).encode("utf-8")
        print("Wysłano do serwera:", data)
        self.sendMessage(data)

        self.users.show()
        self.users.exec_()
>>>>>>> 62d6cb41aded014489af5c2c0f2ee42b4d8629a8


    def listening(self):
        print("Zaczalem sluchac lalalal...")
        self._is_running = True
        while (self._is_running):
            print("Słucham jaaaa")
            try:
                packet, address = self.s.recvfrom(self.size)
                print("Slucham")
                received = json.loads(packet)
                print("Dostałem wiadomość od serwera", received)
                if(str(received["type"]) == "d"):
                    print(received)
                    if received["status"] == 200:
                        print("200")

                    if (received["status"] == 200) and (received["answer_to"] == "LOGIN"):
                        print("Dostalem 200")
                        self.show_add_users()

                    if received["status"] == 406:
                        print("406")

                    if received["status"] == 202:
                        packet = received["users"]
                        print("Otrzymano ", packet)
                        self.users.add_row_to_list_of_users(packet)

                    if received["status"] == 201:
                        print("201")

                    if received["status"] == 401:
                        print("401")

                    """if packet[0:1] == "d":
                        print("Komunikat: ", packet[2::])
                        print(packet[2:7])
                        
                        if packet[2:8] == "INVITE":
                            print("Dzwoni ", packet[9::])
                            self._is_running = False
                            break"""
                else:
                    continue
            except ConnectionRefusedError as err:
                print(err)


    def login(self, login, password):

        payload = {"type": "d", "description": "LOGIN", "status": 200, "login": login, "password": password}

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)



    def sendingVoice(self):
        print("[*] Recording")
        
        while True:
            
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
               
                print("Wysylanie")
                self.data = "s ".encode("utf-8") + self.stream.read(self.CHUNK)

                if self.data:
                    # Write data to pyaudio stream
                    self.stream.write(self.data)  # Stream the recieved audio data
                    try:
                        print("Wysłano :)")
                        self.s.send(self.data)
                        
                    except ConnectionRefusedError as err:
                        print(err)
                        break
                    
        print("[*] Stop recording")

    def closeConnection(self):

        self.stream.stop_stream()
        self.stream.close()
        self.s.close()

