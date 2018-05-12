import pyaudio
import socket
#from JaroEliCall.src.validation import Validator


#class Client(Validator):
class Client:
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    WIDTH = 1
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 15
    FACTOR = 2

    #def __init__(self, priv, publ):

    def __init__(self):
        print("Inicjalizacja klasy Client")

        """self.__private_key = priv
        self.__public_key = publ"""

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

    def connectToSerwer(self, host):
        # ipadres serwera
        self.host = host
        self.port = 50001
        self.size = 2048

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.connect((self.host, self.port))
        except ConnectionRefusedError as err:
            print(err)
            self.s.close()

    def sendMessage(self, data):
        print("Wiadomosc do wyslania: ", data)
        try:
            self.s.sendto(data, (self.host, self.port))
            print("Wiadomosc wyslana")
            packet, address= self.s.recvfrom(self.size)
            print("wiadomosc odebrana", packet)
        except ConnectionRefusedError as err:
            print(err)
        print("Czekam na odpowiedź od serwera 200/406")

    def wait4Response(self):
        while True:
            try:
                print("Oczekiwanie....")
                data, addr2 = self.s.recvfrom(self.size)
                data = data.decode("utf-8")
                print(data[0:3])
                if(data[0:3] == "200"):
                    return 1
                elif (data[0:3]=="406"):
                    return 0
                elif(data[0:3] == "202"):
                    return data
            except ConnectionRefusedError:
                print("Blad przy otrzymywaniu odp od serwera")


    def login(self, login, password):
        value = login + " " + password
        # v = self.signData(value)
        data = ("LOGIN " + socket.gethostbyname(socket.gethostname()) + " " + str(value)).encode("utf-8")
        print(data)
        self.sendMessage(data)
        #self.wait4Response()




    def sendingVoice(self):


        print("[*] Recording")
        while True:
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                print("Wysylanie")
                #self.data = self.stream.read(self.CHUNK)

                if self.data:
                    # Write data to pyaudio stream
                    #self.stream.write(self.data)  # Stream the recieved audio data
                    try:
                        print("Wysłano :)")
                        self.s.send(self.data)
                    except ConnectionRefusedError as err:
                        print(err)
                        break
        print("[*] Stop recording")

    def closeConnection(self):

        # print(type(data), data)

        # stream.write(data, CHUNK)
        self.stream.stop_stream()
        self.stream.close()
        self.s.close()

"""
cl = Client()
cl.connectToSerwer('192.168.0.102')
cl.sendingVoice()"""
