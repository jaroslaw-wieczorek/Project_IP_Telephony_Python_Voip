
import os
import sys

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

import pyaudio
import socket
import json
import threading


class Client:
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 2
    FACTOR = 2
    

    def __init__(self, SERWER_IP, port):
        print("Inicjalizacja klasy Client")
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)
        
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


    def listening_all(self, port):
        ip = ''
        socket = socket.socket()
        socket.connect((ip, int(port)))
        print("\tClinet : info >> Listen IP:", str(ip), "PORT:", str(port))
        while 1:
            data = socket.recv(2048)
            print("\tClinet : info >> Got message:", data, "from:", str(ip))


    def listening(self, toThreaad):
        print("\tClinet : info >> Setup listening")
        self._is_running = True
        print("\tClinet : info >> Set _is_running on True")
        while self._is_running:
            
            print("\tClinet : info >> Listen now")
            packet, address = self.socket.recvfrom(self.size)
            packet = packet.decode("utf-8")
            received = json.loads(packet)
            
            print("\tClinet : info >> Get response from server", received)
            if(str(received["type"]) == "d"):
                
                with toThreaad.lock:

                    if (received["status"] == 200) and (received["answer_to"] == "LOGIN"):
                        print("Dostalem 200")
                        toThreaad.received = ("200 LOGIN")
                        break

                    if received["status"] == 200 and received["answer_to"] == "NOTHING":
                        toThreaad.received = ("200 NOTHING " + str(received["from_who"]))
                        print("200 INVITE ", received["from_who"])
                        print("Dzwoni ", str(received["from_who"]))
                        break

                    if received["status"] == 200 and received["answer_to"] == "INVITE":
                        toThreaad.received = ("200 INVITE " + str(received["IP"]))
                        print("200 INVITE ", received["IP"])
                        break


                    if received["status"] == 406 and received["answer_to"] == "INVITE":
                        toThreaad.received = ("406 INVITE")
                        print("406")
                        break


                    if received["status"] == 406 and received["answer_to"] == "LOGIN":
                        toThreaad.received = ("406 LOGIN")
                        print("406")
                        break
                    

                    if received["status"] == 406 and received["answer_to"] == "CREATE":
                        toThreaad.received = ("406 NOT_CREATED")
                        print("406")
                        break


                    if received["status"] == 201 and received["answer_to"] == "CREATE":
                        toThreaad.received = ("201 CREATED")
                        break


                    if received["status"] == 202:
                        packet = received["users"]
                        print("Otrzymano ", packet)
                        toThreaad.received = ("202 USERS")
                        toThreaad.users = packet
                        break


                    if received["status"] == 401:
                        print("401")
                        break


                    if received["status"] == 200 and received["answer_to"] == "LOGOUT":
                        toThreaad.received = ("200 LOGOUT")
                        print("200")
                        break

                        """if packet[0:1] == "d":
                            print("Komunikat: ", packet[2::])
                            print(packet[2:7])
                            
                            if packet[2:8] == "INVITE":
                                print("Dzwoni ", packet[9::])
                                self._is_running = False
                                break"""
                        print("\tClinet : warrning >> Still listen")
                    else:
                        continue


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
        