from socket import *
import pyaudio
import wave


class Client:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 40

    def __init__(self, login, password):
        self.login = login
        self.password = password
        #record
        self.s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
        self.s.connect(('192.168.0.103', 8888)) # nawiazanie polaczenia

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("*recording")

        self.loginPass()

    def loginPass(self):
        self.frames = []

        data = (self.login + " " + self.password).encode()
        self.frames.append(data)
        self.s.sendall(data)
        print(data)

    def sendVoice(self):
        #idzie echo 3 razy gdy jest while(True):
        for i in range(0, int(self.RATE/self.CHUNK*self.RECORD_SECONDS)):
            data  = self.stream.read(self.CHUNK)
            self.frames.append(data)
            self.s.sendall(data)
            print(data)

    def closeConnection(self):
        print("*done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.s.close()

        print("*closed")