
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:20:23 2018

@author: afar
"""

import pyaudio
import audioop
from collections import OrderedDict
import socket
import time 


FORMAT = pyaudio.paInt16
CHUNK = 160
#WIDTH = 1
CHANNELS = 1
RATE = 44100
#RECORD_SECONDS = 15
#FACTOR = 2

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("[*] Recording")

####

host = '192.168.43.70'
port = 50002
size = 2048


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host,port))
except ConnectionRefusedError as err:
    print(err)
    s.close()


while True:
#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
   
    if data:
        # Write data to pyaudio stream
        #stream.write(data)  # Stream the recieved audio data
        try:
            s.send(data)
        except ConnectionRefusedError as err:
            print(err)
            break
            
    
    # print(type(data), data)
     
    #stream.write(data, CHUNK)
print("[*] Stop recording")

stream.stop_stream()
stream.close()
s.close()
