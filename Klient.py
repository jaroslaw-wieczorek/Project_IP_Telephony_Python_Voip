# -*- coding: utf-8 -*-

import pyaudio
import socket
import sys
import time

# Pyaudio Initialization
chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
 
p = pyaudio.PyAudio()
 
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)
 
# Socket Initialization
host = 'localhost'
port = 50001
size = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host,port))
 
# Main Functionality
while 1:
    data = stream.read(chunk)
    s.send(data)
    s.recvfrom(size)
 
s.close()
stream.close()
p.terminate()