#!/usr/bin/env python
import pyaudio
import socket
import sys

# Pyaudio Initialization
chunk = 2048
rate = 8000
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=rate,
                output=True)

# Socket Initialization
host = ''
port = 50002
#rozmiar jaki otrzymuje serwer musi byc wiekszy niż to co wysyla klient
size = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

# Main Functionality
while 1:
    data, addr = s.recvfrom(size)
    if data:
        # Write data to pyaudio stream
        stream.write(data)  # Stream the recieved audio data
        s.sendto(data, addr)

s.close()
stream.close()
p.terminate()