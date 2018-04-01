#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:36:24 2018

@author: afar
"""
import scapy 
import socket
from socket import *


import sys
import wave
import audioop
import pyaudio



CHANNELS = 1
RATE = 8000
CHUNK = 500
FORMAT = pyaudio.paInt16


def audio_int(num_samples=50):

    """Pozwala uzyskać średnią intensywność dźwięku z mikrofonu. 
       Za jego pomocą można uzyskać średnie natężenie dźwięku podczas rozmowy i/lub w ciszy.
       Średnia jest średnią z największych odnotowanych intensywności na poziomie 20%.
    """
    

    print("Getting intensity values from mic.")
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    values = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 4)))
              for x in range(num_samples)]
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    print("Finished")
    print("Average audio intensity is ", r)
    
    stream.close()
    p.terminate()

    return r 

pyaudio.PlayAudio(r)