#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:22:22 2018

@author: afar
"""
import os
import sys
import pyaudio
import socket
import asyncio
from threading import Thread

"""
class MyUDPServer(asyncio.DatagramProtocol):
...
    def connection_made(self, transport):
        self.transport = transport

        # Allow receiving multicast broadcasts
        sock = self.transport.get_extra_info('socket')
        group = socket.inet_aton('239.255.255.250')
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
"""

class MyVOIPProtocol(asyncio.DatagramProtocol):
    FORMAT = pyaudio.paInt16
    CHUNK = 512
    WIDTH = 1
    CHANNELS = 1
    RATE = 16000
    FACTOR = 1
    
    def __init__(self, loop):

        self.loop = loop
        self.transport = None
        
        self.host = '127.0.0.1'
        self.port = 9999
        self.size = 2048
        
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.CHUNK)

        
        super().__init__()
    
    def send_voice(self):
        self.voice_msg =  self.stream.read(self.CHUNK)
        print("record chunk")
        self.transport.sendto(self.voice_msg)
                      
    def connection_made(self, transport):
        self.transport = transport
        self.send_voice()
        
    def datagram_received(self, data, addr):
        print("Recived from: ", addr)
        self.stream.write(data)
        print("stream write done")
    
    def error_received(self, exc):
        print('Error received:', exc)
        
        
    def stop_call(self):        
        self.stream.stop_stream()
        self.stream.close()


loop = asyncio.get_event_loop()
#loop.create_task(MyVOIPProtocol(loop).foo())
connect = loop.create_datagram_endpoint(
        lambda: MyVOIPProtocol(loop),
        remote_addr=('127.0.0.1', 9999))

loop.run_until_complete(connect)
loop.run_forever()

#transport.close()
#loop.close()

