from pylab import*
from scipy.io import wavfile

print("Analyze audio used scipy.io wavfile")
print("sampFreq, snd = wavfile.read('440_sine.wav')")
sampFreq, snd = wavfile.read('440_sine.wav')

print("sampFreq, snd[0:30]:", sampFreq, snd[0:30])

print("print(snd.dtype)", snd.dtype)

snd = snd / (2.**15)
print("snd = snd / (2.**15), snd[0:30]", snd[0:30])

print("snd.shape", snd.shape)

print("5292 / sampFreq:", 5292 / sampFreq)

s1 = snd[:,0]

print(s1)
