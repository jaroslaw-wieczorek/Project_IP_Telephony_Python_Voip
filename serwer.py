
from socket import *
import pyaudio
import wave
import time

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

