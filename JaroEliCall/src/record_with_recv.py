import pyaudio
import socket
from pymongo import MongoClient
import rsa

class Serwer:
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    WIDTH = 1
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 15
    FACTOR = 2

    def __init__(self):
        print("Inicjalizacja klasy ")

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=self.CHUNK)

    def connectWithClient(self):
        print("Nawiazanie połączenia")
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

                try:
                    data = data.decode("utf-8")
                    frames = data.split(" ")
                    print(frames)
                    de = rsa.Encrypt()
                    de.decode(frames)
                    if(data[0:6] == "INVITE"):
                        ans = self.checkWithMongo(data)
                        if(ans == 1):
                            print("Logowanie ok")
                            #komunikat o pomyslnym logowaniu
                            break
                       # elif (ans == 0):
                            #komunikat o niepoprawnym logowaniu

                    # Write data to pyaudio stream
                    #stream.write(data)  # Stream the recieved audio data
                except UnicodeDecodeError as e:
                    raise


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
        db = client['BomberMan']
        collection = db['Players']

        print(data)
        frames = (data.split())


        answer = (collection.find({"login": frames[0], "password": frames[1]}).count()) == 1

        if (answer):
            return 1
        else:
            return 0



serwer = Serwer()
serwer.connectWithClient()
serwer.listening()
serwer.stopConnection()

