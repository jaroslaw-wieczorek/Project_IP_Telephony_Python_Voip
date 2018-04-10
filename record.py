import pyaudio
import audioop
from collections import OrderedDict

import time 


FORMAT = pyaudio.paInt16
CHUNK = 1024
WIDTH = 4
CHANNELS = 1
RATE = 16000
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
    new_frames = audioop.lin2ulaw(data, 1)
    #print(type(data), data)
    #print(new_frames)
    stream.write(new_frames, CHUNK)
    #stream.write(data, CHUNK)
print("[*] Stop recording")

stream.stop_stream()
stream.close()

