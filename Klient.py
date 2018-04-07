from socket import *
import pyaudio
import wave


class Client:
    def __init__(self, login, password):
        #record
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 40

        s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
        s.connect(('192.168.0.103', 8888)) # nawiazanie polaczenia

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*recording")

        frames = []


        data = (login+" "+password).encode()
        print(data.split())
        frames.append(data)
        s.sendall(data)
        print(data)

        """for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
         data  = stream.read(CHUNK)
         frames.append(data)
         s.sendall(data)
         print(data)"""

        print("*done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()
        s.close()

        print("*closed")