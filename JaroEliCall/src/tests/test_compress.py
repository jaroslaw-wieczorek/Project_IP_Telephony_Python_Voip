import numpy
import time
from numpy import zeros
from numpy import float32
from pyaudio import PyAudio, paFloat32


class Limiter:
    def __init__(self, attack_coeff, release_coeff, delay, dtype=float32):
        self.delay_index = 0
        self.envelope = 0
        self.gain = 1
        self.delay = delay
        self.delay_line = zeros(delay, dtype=dtype)
        self.release_coeff = release_coeff
        self.attack_coeff = attack_coeff

    def limit(self, signal, threshold):
        for i in arange(len(signal)):
            self.delay_line[self.delay_index] = signal[i]
            self.delay_index = (self.delay_index + 1) % self.delay

            # calculate an envelope of the signal
            self.envelope *= self.release_coeff
            self.envelope  = max(abs(signal[i]), self.envelope)

            # have self.gain go towards a desired limiter gain
            if self.envelope > threshold:
                target_gain = (1+threshold-self.envelope)
            else:
                target_gain = 1.0
                self.gain = ( self.gain*self.attack_coeff +
                              target_gain*(1-self.attack_coeff) )

            # limit the delayed signal
            signal[i] = self.delay_line[self.delay_index] * self.gain
       
    
     
def callback(in_data, frame_count, time_info, flag):
    if flag:
        print("Playback Error: %i" % flag)
    played_frames = 0
    counter += frame_count
    limiter.limit(signal[played_frames:counter], threshold)
    return signal[played_frames:counter], paContinue               
                
                

attack_coeff = 4
  
release_coeff = 10

delay = 1
             
limiter = Limiter(attack_coeff, release_coeff, delay, float32)

    
pa = PyAudio()

stream = pa.open(format = paFloat32,
                     channels = 1,
                     rate = 44100,
                     output = True,
                     frames_per_buffer = 1024,
                     stream_callback = callback)


while stream.is_active():
    time.sleep(0)

    stream.close()
    pa.terminate()