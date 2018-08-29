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
    def __init__(self, threadID, name, counter, rport, event):
        threading.Thread.__init__(self)
        self.daemon = True
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.REMOTE_PORT = rport
        self.p = pyaudio.PyAudio()
        self.queue = Queue()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)
        super()
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_status = ""

        self.stopped = event

    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        self.socket_status = "open"

        self.serverSide()
        # Free lock to release next thread
        # threadLock.release()

    def serverSide(self):
        # ip local computer
        # serverIP = socket.gethostbyname(socket.gethostname())
        global serverIP

        self.serverSocket.bind((serverIP, self.REMOTE_PORT))
        print("Listen on: ", serverIP, self.REMOTE_PORT)
        time.sleep(2)

        while True:
            if self.socket_status == "open":
                if not self.stopped.is_set():
                    message, clientAddress = self.serverSocket.recvfrom(
                        self.CHUNK * 2)
                    print(message)
                    self.queue.put(message)
                    self.stream.write(self.queue.get())
                    # mx = audioop.max(message, 2)
                    # print(mx)


    def close_serverSocket(self):
        self.socket_status = "close"
        print(type(self.serverSocket))
        self.stream.close()
        self.serverSocket.close()
        print("Close server socket")


class ClientThread(threading.Thread, Configuration):
    def __init__(self, threadID, name, counter, rip, rport, event):
        threading.Thread.__init__(self)
        self.daemon = True
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
        self.socket_status = ""

        self.stopped = event
        super()

    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        self.socket_status = "open"
        self.clientSide()
        # Free lock to release next thread
        # threadLock.release()

    def clientSide(self):

        print("Send on: ", self.REMOTE_IP, self.REMOTE_PORT)
        self.clientSocket.connect((self.REMOTE_IP, self.REMOTE_PORT))
        time.sleep(2)
        while True:
            if self.socket_status == "open":
                if not self.stopped.is_set():
                    message = self.stream.read(self.CHUNK)
                    print(message)
                    self.queue.put(message)
                    self.clientSocket.send(self.queue.get())
                    # mx = audioop.max(message, 2)
                    # print(mx)

    def close_clientSocket(self):
        self.socket_status = "close"
        print(type(self.clientSocket))
        self.stream.close()
        self.clientSocket.close()
        print("Close client socket")
