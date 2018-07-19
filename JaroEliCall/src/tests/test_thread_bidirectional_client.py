#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 07:08:27 2018

@author: afar
"""

import socket
import base64
import json 
import time

IP, PORT = '127.0.0.1', 4247

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)


sock.sendto("connection".encode(), (IP, PORT))

while True:
    msg, b = sock.recvfrom(1024)
    print(msg.decode())
    
    time.sleep(3)
    sock.sendto("get data".encode(), (IP, PORT))