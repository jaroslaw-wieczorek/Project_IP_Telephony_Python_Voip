#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 16:38:14 2018

@author: afar
"""

import time
import wave
import pyaudio
import logging
import threading 




class RecordThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        
        logging.debug('Record thread init with %s and %s',
                      self.args, self.kwargs)
        

        self.setupAudioStream()


    def run(self):
        logging.debug('Record Thread running with %s and %s',
                      self.args, self.kwargs)
        self.record()


    def setupAudioStream(self):
        logging.debug('setup audio conf')
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.FRAMES = None
        self.WAVE_OUTPUT_FILENAME = "demo.wav"

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK,
                                  stream_callback=self.get_callback
                                  )
        
        self.wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        self.wf.setnchannels(self.CHANNELS)
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        self.wf.setframerate(self.RATE)
        
        print("RecordThread - End setup")
   #     self.wf.writeframes(b''.join(self.frames))


    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wf.writeframes(in_data)
            data = self.wf.readframes(frame_count)
            return data, pyaudio.paContinue
        return callback


    def record(self):
        self.frames = []
        while True:
            self.data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            
            print("RecordThread data:", self.data)
   
    
    def stop(self):
        print("RecordThread stop")
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()
        self.p.terminate()
    

        

class PlayThread(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        
        
        logging.debug('Play thread init with %s and %s',
                      self.args, self.kwargs)
        
        self.setupAudioStream()
        
        
    def run(self):
        logging.debug('running with %s and %s',
                      self.args, self.kwargs)
        self.play()
        
        
    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            data = self.wf.readframes(frame_count)
            print("play")
            return data, pyaudio.paContinue
        return callback


    def setupAudioStream(self):
        
        logging.debug('setup audio conf')
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.WAVE_OUTPUT_FILENAME = "demo.wav"
        
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK, 
                                  stream_callback=self.get_callback)
    def play(self):
        self.stream.start_stream()
            
        while self.stream.is_active():
            time.sleep(0.1)

    def stop(self):
        print("STOP")
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()
        self.p.terminate()

        