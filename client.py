# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:20:23 2018

@author: afar
"""

import pyaudio
import socket


from validation import Validator

from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64encode, b64decode 


class Client(Validator):
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    WIDTH = 1
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 15
    FACTOR = 2
    
    
    def __init__(self, priv, publ):
        Validator.__init__(self,priv,publ)
        print("Inicjalizacja klasy Client")
        
        self.__private_key = priv
        self.__public_key = publ
        
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=self.CHUNK)

    def connectToSerwer(self):
        #ipadres serwera
        host = '192.168.0.102'
        port = 50001
        self.size = 2048


        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.connect((host,port))
        except ConnectionRefusedError as err:
            print(err)
            self.s.close()


    def login(self, login, password):

        value = login + " " + password
        v = self.signData(value)
        self.data = ("INVITE " +socket.gethostbyname(socket.gethostname()) + " " + str(v)).encode("utf-8")

        #Encryption

        print(self.data)
        try:
            self.s.send(self.data)
        except ConnectionRefusedError as err:
            print(err)


    def sendingVoice(self):
        print("[*] Recording")


        while True:
        #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            self.data = self.stream.read(self.CHUNK)

            if self.data:
                # Write data to pyaudio stream
                #stream.write(data)  # Stream the recieved audio data
                try:
                    self.s.send(self.data)
                except ConnectionRefusedError as err:
                    print(err)
                    break
        print("[*] Stop recording")


    def closeConnection(self):

        # print(type(data), data)

        #stream.write(data, CHUNK)
        self.stream.stop_stream()
        self.stream.close()
        self.s.close()



