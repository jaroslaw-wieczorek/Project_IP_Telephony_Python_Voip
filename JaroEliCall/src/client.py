import pyaudio
import socket
from JaroEliCall.src.actionsViews.Interaction_code import InteractionWidget

from threading import Thread
#class Client(Validator):
class Client:
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
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
        print("Laczrenie z serwerem")
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
        print("Wiadomosc do wyslania do serwera: ", self.host)
        try:
            self.s.sendto(data, (self.host, self.port))
            print("Wiadomosc wyslana. Czekam na odp")
            packet, address = self.s.recvfrom(self.size)
            if (packet):
                packet = packet.decode("utf-8")
                print("wiadomosc odebrana", packet)
                if (packet[0:3] == "200"):
                    return 1
                elif (packet[0:3] == "406"):
                    return 0
                elif (packet[0:3] == "202"):
                    return packet
                elif (packet[0:3] == "201"):
                    return 1
        except ConnectionRefusedError as err:
            print(err)

    def listening(self):
        print("Zaczalem sluchac lalalal...")
        while 1:
            try:
                packet, address = self.s.recvfrom(self.size)
                if (packet):
                    packet = packet.decode("utf-8")
                    print("wiadomosc odebrana", packet)
                    if (packet[0:1] == "d"):
                        print("Komunikat: ", packet[2::])
                        print(packet[2:7])
                        if(packet[2:8] == "INVITE"):
                            print("Dzwoni ", packet[9::])
                            connection = InteractionWidget(packet[9::])
                            connection.show()
                            connection.exec_()
                else: continue
            except ConnectionRefusedError as err:
                print(err)

    def login(self, login, password):
        value = login + " " + password
        # v = self.signData(value)
        print("Proba wyslania")
        data = ("d LOGIN " + socket.gethostbyname(socket.gethostname()) + " " + str(value)).encode("utf-8")
        print(data)
        return self.sendMessage(data)


    def sendingVoice(self):
        print("[*] Recording")
        while True:
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                print("Wysylanie")
                self.data = "s ".encode("utf-8") + self.stream.read(self.CHUNK)

                if self.data:
                    # Write data to pyaudio stream
                    self.stream.write(self.data)  # Stream the recieved audio data
                    try:
                        print("Wysłano :)")
                        self.s.send(self.data)
                    except ConnectionRefusedError as err:
                        print(err)
                        break
        print("[*] Stop recording")

    def closeConnection(self):

        self.stream.stop_stream()
        self.stream.close()
        self.s.close()
