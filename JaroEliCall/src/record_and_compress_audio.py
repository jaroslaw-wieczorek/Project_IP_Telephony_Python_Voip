#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:22:34 2018

@author: afar
"""

import wave

from pyaudio import PyAudio
from pyaudio import paFloat32
from pyaudio import paContinue


from sys import byteorder
from time import sleep
from array import array
from struct import pack

from numpy import zeros
from numpy import array 
from numpy import random
from numpy import arange
from numpy import float32
from numpy import float64

################################### Recording ##################################
    
FORMAT = pyaudio.paInt16
CHUNK = 512
WIDTH = 1
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 15
FACTOR = 2

#THRESHOLD = 0.8
#DELAY = 40

#RELEASE_COEFF = 0.9999
#ATTACK_COEFF  = 0.9
#DTYPE = float32
#BLOCK_LEN = 512


################################### Constants ##################################

fs            = 44100   # Hz
threshold     = 0.8     # absolute gain
delay         = 40      # samples
signal_length = 1       # second
release_coeff = 0.9999  # release time factor
attack_coeff  = 0.9     # attack time factor
dtype         = float32 # default data type
block_length  = 512     # samples





"""
class Limiter:
    def __init__(self, attack_coeff, release_coeff, delay, dtype=float32):
        self.delay_index = 0
        self.envelope = 0
        self.gain = 1
        self.delay = delay
        self.delay_line = zeros(delay, dtype=dtype)
        self.release_coeff = release_coeff
        self.attack_coeff = attack_coeff
"""      
        


