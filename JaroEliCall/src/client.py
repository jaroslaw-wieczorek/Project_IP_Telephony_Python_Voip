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
        print("Wiadomosc do wyslania do: ", self.host)
        try:
            self.s.sendto(data, (self.host, self.port))
            print("Wiadomosc wyslana. Czekam na odp")
            packet, address= self.s.recvfrom(self.size)
            if(packet):
                packet = packet.decode("utf-8")
                print("wiadomosc odebrana", packet)
                if (packet[0:3] == "200"):
                    return 1
                elif (packet[0:3] == "406"):
                    return 0
                elif (packet[0:3] == "202"):
                    return packet
        except ConnectionRefusedError as err:
            print(err)

    def login(self, login, password):
        value = login + " " + password
        # v = self.signData(value)
        data = ("d LOGIN " + socket.gethostbyname(socket.gethostname()) + " " + str(value)).encode("utf-8")

        print(data)
        return self.sendMessage(data)

    def sendingVoice(self):
        print("[*] Recording")
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            while True:
                print("Wysylanie")
                self.data = "s ".encode("utf-8") + self.stream.read(self.CHUNK)

                if self.data:
                    # Write data to pyaudio stream
                    # self.stream.write(self.data)  # Stream the recieved audio data
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
