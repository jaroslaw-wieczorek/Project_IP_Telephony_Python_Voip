
import os
import sys
import time
import socket
import asyncio
import pyaudio
import audioop
import threading
from datetime import datetime


class Configuration():
        FORMAT = pyaudio.paInt16
        CHUNK = 1024
        WIDTH = 2
        CHANNELS = 1
        RATE = 16000
        FACTOR = 1
        REMOTE_IP = None
        REMOTE_PORT = None
    


class ServerThread (threading.Thread, Configuration):
    def __init__(self, threadID, name, counter, rport ):
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
        print ("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        serverSide(self.REMOTE_PORT, self.stream, self.CHUNK)
        # Free lock to release next thread
        # threadLock.release()
        
        

class ClientThread (threading.Thread, Configuration):
   
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
        print ("Starting: " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        clientSide(self.REMOTE_IP, self.REMOTE_PORT, self.stream, self.CHUNK)
        # Free lock to release next thread
        # threadLock.release()



def serverSide(rport,stream, chunk):
    # ip local computer
    serverIP = '127.0.0.1'
    serverPort = rport
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverIP,serverPort))
    print("Listen on: ", serverIP, serverPort)
    time.sleep(2)
    while True:
        message, clientAddress = serverSocket.recvfrom(chunk*2)
        stream.write(message)
        mx = audioop.max(message, 2)
        print(mx)




def clientSide(ip, port, stream, chunk):
    serverIP = ip
    serverPort = port
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Send on: ", serverIP, serverPort)
    time.sleep(2)
    while True:
        message = stream.read(chunk)
        clientSocket.sendto(message,(serverIP, serverPort))
        mx = audioop.max(message, 2)
        print(mx)
    #clientSocket.close() # Close the socket

# threadLock = threading.Lock()

"""
threads = []

# IP remote computer
IP = '127.0.0.1'

# Create new threads
thread1 = ServerThread(1, "Server-Thread", 1, 9999)
thread2 = ClientThread(2, "Client-Thread", 2, IP, 9999 )

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
    
print ("Exiting Main Thread")
"""