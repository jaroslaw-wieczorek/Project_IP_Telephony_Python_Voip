from socket import *
import pyaudio
import wave
import time
import pprint
import hashlib
from pymongo import MongoClient



def checkWithMongo(data):
    nick, password = data.split()
    nick, password = nick.decode("utf-8"), password.decode("utf-8")
    print(nick, password)
    client = MongoClient('localhost', 27017)
    db = client['VOIP']
    collection = db['Users']

    answer = (collection.find({"login": nick, "password": password}).count())
    print(answer)

    if (answer):
        result = collection.update({"login": nick, "password": password}, {'$set': {'status': 'available'}})
        print(result)
        return 1
    else:
        return 0



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
frames = []

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
s.bind(('', 8888)) # nawiazanie polaczenia
s.listen(5) #Wait for the client connection
print("Zainicjowano polaczenie")

i=1

while True:
    c,addr = s.accept() #Establish a connection with the client
    print("Got connection from", addr)
    data = c.recv(1024)
    checkWithMongo(data)


    while data != '':
        stream.write(data)
        data = c.recv(1024)
        print(data)
        i = i + 1
        frames.append(data)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(''.join(frames))
    wf.close()

    stream.stop_stream()
    stream.close()
    p.terminate()
    c.close()