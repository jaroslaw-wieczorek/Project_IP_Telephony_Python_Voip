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
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.daemon = True
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.p = pyaudio.PyAudio()
        self.queue = None
        self.stream = None
        self.REMOTE_PORT = None
        self.serverSocket = None
        super()

    def setup(self, port_serwer):
        self.queue = Queue()
        self.REMOTE_PORT = port_serwer
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.stopped = threading.Event()

    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()

        self.serverSide()
        # Free lock to release next thread
        # threadLock.release()

    def serverSide(self):
        # ip local computer
        # serverIP = socket.gethostbyname(socket.gethostname())
        global serverIP
        print("<*> ServerThread info: listen on: (%s,%d)" % (serverIP, self.REMOTE_PORT))
        self.serverSocket.bind((serverIP, self.REMOTE_PORT))
        print("Listen on: ", serverIP, self.REMOTE_PORT)
        time.sleep(2)

        while not self.stopped.is_set():
            try:
                message, clientAddress = self.serverSocket.recvfrom(
                    self.CHUNK * 2)
                print("<<*>> ThreadSide Odbieranie: " + str(message)[0:5])
                print()
                self.queue.put(message)
                self.stream.write(self.queue.get())
                # mx = audioop.max(message, 2)
                # print(mx)
            except Exception as err:
                print("<!> ServerThread ERROR:\n\t", err)

    def close_serverSocket(self):
       
        print(type(self.serverSocket))
        #self.stream.stop_stream()
        self.serverSocket.close()
        print("Close server socket")


class ClientThread(threading.Thread, Configuration):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.daemon = True
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.p = pyaudio.PyAudio()
        self.queue = None
        self.stream = None
        self.stopped = None
        self.clientSocket = None

    def setup(self, rip, rport):
        self.queue = Queue()
        self.REMOTE_IP = rip[0]
        self.REMOTE_PORT = rport
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.stopped = threading.Event()

    def run(self):

        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()

        self.clientSide()
        # Free lock to release next thread
        # threadLock.release()

    def clientSide(self):
        print("<*> ClientThread info: Send on: ", self.REMOTE_IP, self.REMOTE_PORT)
        self.clientSocket.connect((self.REMOTE_IP, self.REMOTE_PORT))
        time.sleep(2)

        while not self.stopped.is_set():
            try:
                message = self.stream.read(self.CHUNK)
                print("<<*>> ClientSide wysylanie: " + str(message)[0:5])
                print()
                self.queue.put(message)
                self.clientSocket.send(self.queue.get())
                # mx = audioop.max(message, 2)
                # print(mx)

            except Exception as err:
                print("<!> ClientThread ERROR:\n\t", err)

    def close_clientSocket(self):
       
        print(type(self.clientSocket))
        #self.stream.stop_stream()
        #self.stream.close()
        self.clientSocket.close()