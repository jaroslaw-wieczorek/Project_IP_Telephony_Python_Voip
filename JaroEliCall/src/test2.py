import os
import sys
import time
import socket
import pyaudio
import audioop
import threading
from queue import Queue

serverIP = "0.0.0.0"

class Configuration():
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 2
    CHANNELS = 1
    RATE = 16000
    FACTOR = 1
    REMOTE_IP = None
    REMOTE_PORT = None


class ServerThread(threading.Thread, Configuration):
    def __init__(self, threadID, name, counter, rport):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.REMOTE_PORT = rport
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)
        super()
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        self.serverSide()
        # Free lock to release next thread
        # threadLock.release()


    def serverSide(self):
        # ip local computer
        #serverIP = socket.gethostbyname(socket.gethostname())
        global serverIP

        self.serverSocket.bind((serverIP, self.REMOTE_PORT))
        print("Listen on: ", serverIP, self.REMOTE_PORT)
        time.sleep(2)

        while True:
            if self.serverSocket:
                message, clientAddress = self.serverSocket.recvfrom(self.CHUNK * 2)
                self.stream.write(message)
                mx = audioop.max(message, 2)
                # print(mx)

    def close_serverSocket(self):
        self.serverSocket.close()


class ClientThread(threading.Thread, Configuration):

    def __init__(self, threadID, name, counter, rip, rport):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.REMOTE_IP = rip[0]
        self.REMOTE_PORT = rport
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.queue = Queue()

        super()

    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        self.clientSide()
        # Free lock to release next thread
        # threadLock.release()

    def clientSide(self):

        print("Send on: ", self.REMOTE_IP, self.REMOTE_PORT)
        self.clientSocket.connect((self.REMOTE_IP,  self.REMOTE_PORT))
        time.sleep(2)
        while True:
            if self.clientSocket:
                message = self.stream.read(self.CHUNK)
                self.clientSocket.send(message)
                mx = audioop.max(message, 2)
                # print(mx)

    def close_clientSocket(self):
        self.clientSocket.close()
