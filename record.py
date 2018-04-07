import pyaudio
import audioop
from collections import OrderedDict



FORMAT = pyaudio.paInt16
CHUNK = 1024
WIDTH = 1
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 15
FACTOR = 2    



p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("[*] Recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
  
     
    stream.write(data, CHUNK)
print("[*] Stop recording")

stream.stop_stream()
stream.close()

