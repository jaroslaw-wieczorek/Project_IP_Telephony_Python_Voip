import alsaaudio as audio
import time
import audioop


#Input & Output Settings
periodsize = 1024
audioformat = audio.PCM_FORMAT_FLOAT_LE
channels = 16
framerate=8000

#Input Device
inp = audio.PCM(audio.PCM_CAPTURE,audio.PCM_NONBLOCK,device='hw:1,0')
inp.setchannels(channels)
inp.setrate(framerate)
inp.setformat(audioformat)
inp.setperiodsize(periodsize)

#Output Device
out = audio.PCM(audio.PCM_PLAYBACK,device='hw:0,0')
out.setchannels(channels)
out.setrate(framerate)
out.setformat(audioformat)
out.setperiodsize(periodsize)


#Reading the Input
allData = bytearray()
count = 0
while True:
    #reading the input into one long bytearray
    l,data = inp.read()
    for b in data:
        allData.append(b)

    #Just an ending condition
    count += 1
    if count == 4000:
        break

    time.sleep(.001)

