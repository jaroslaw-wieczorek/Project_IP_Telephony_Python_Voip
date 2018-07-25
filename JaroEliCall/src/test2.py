import os
import sys
import time
import socket
import pyaudio
import audioop
import threading

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

        self.stream = self.p.open(format=self.p.get_format_from_width(self.WIDTH),
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)
        super()

    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        serverSide(self.REMOTE_PORT, self.stream, self.CHUNK)
        # Free lock to release next thread
        # threadLock.release()


class ClientThread(threading.Thread, Configuration):
    def __init__(self, threadID, name, counter, rip, rport):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.REMOTE_IP = rip
        self.REMOTE_PORT = rport
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

        super()

    def run(self):
        print("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        clientSide(self.REMOTE_IP, self.REMOTE_PORT, self.stream, self.CHUNK)
        # Free lock to release next thread
        # threadLock.release()


def serverSide(rport, stream, chunk):
    # ip local computer
    serverIP = socket.gethostbyname(socket.gethostname())

    serverPort = rport
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverIP, serverPort))
    print("Listen on: ", serverIP, serverPort)
    time.sleep(2)
    while True:
        message, clientAddress = serverSocket.recvfrom(chunk * 2)
        stream.write(message)
        mx = audioop.max(message, 2)
        # print(mx)


def clientSide(ip, port, stream, chunk):
    serverIP = ip[0]
    serverPort = port
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Send on: ", serverIP, serverPort)
    time.sleep(2)
    while True:
        message = stream.read(chunk)
        clientSocket.sendto(message, (serverIP, serverPort))
        mx = audioop.max(message, 2)
        # print(mx)
        # clientSocket.close() # Close the socket




