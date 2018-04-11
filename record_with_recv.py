import pyaudio
import socket
from pymongo import MongoClient

class Serwer:
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    WIDTH = 1
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 15
    FACTOR = 2

    def __init__(self):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=self.CHUNK)

    def connectWithClient(self):
        host = ''
        port = 50001
        self.size = 2048

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.bind((host, port))
        except ConnectionRefusedError as err:
            print(err)
            self.s.close()

    def listening(self):
        print("[*] Start listen")

        while True:
        #for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            try:
                data, addr = self.s.recvfrom(self.size)
            except ConnectionRefusedError as err:
                print(err)
                break

            if data:
                print(data)
                # Write data to pyaudio stream
                self.stream.write(data)  # Stream the recieved audio data
                if(data[0:6] == "INVITE"):
                    data = data.decode("utf-8")
                    ans = self.checkWithMongo(data)
                    if(ans == 1):
                        print("Logowanie ok")
                        #komunikat o pomyslnym logowaniu
                    elif (ans == 0):
                        print("Logowanie nie ok")
                        #komunikat o niepoprawnym logowaniu

                # Write data to pyaudio stream
                #stream.write(data)  # Stream the recieved audio data

            # print(type(data), data)

            #stream.write(data, CHUNK)
        print("[*] Stop listen")

    def stopConnection(self):
        self.stream.stop_stream()
        self.stream.close()
        self.s.close()
        #p.close()

    def checkWithMongo(self, data):
        client = MongoClient('localhost', 27017)
        db = client['VOIP']
        collection = db['Users']

        print(data)
        frames = (data.split())


        answer = (collection.find({"login": frames[2], "password": frames[3]}).count()) == 1
        if (answer == True):
            return 1
        else:
            return 0



serwer = Serwer()
serwer.connectWithClient()
serwer.listening()
serwer.stopConnection()

