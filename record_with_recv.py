import pyaudio
import audioop
from collections import OrderedDict
import socket
import time 

FORMAT = pyaudio.paInt16
CHUNK = 1024
WIDTH = 1
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 15
FACTOR = 2    


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("[*] Start listen")

####

host = 'localhost'
port = 50001
size = 2048

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
except ConnectionRefusedError as err:
    print(err)
    s.close()


while 1:
    try:
        data, addr = s.recvfrom(size)
    except ConnectionRefusedError as err:
        print(err)
        break
               
    if data:
        print(addr)
        # Write data to pyaudio stream
        stream.write(data)  # Stream the recieved audio data

        # Write data to pyaudio stream
        stream.write(data)  # Stream the recieved audio data

    
    # print(type(data), data)
     
    #stream.write(data, CHUNK)
print("[*] Stop listen")

stream.stop_stream()
stream.close()
s.close()
p.close()

