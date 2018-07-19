#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 07:05:09 2018

@author: afar
"""

import threading
import socket
import logging
import json 

class Broker():

    IP, PORT = "127.0.0.1", 4247
    
    def __init__(self):
        logging.info('Initializing Broker')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))
        self.clients_list = []

    def talkToClient(self, ip):
        logging.info("Sending 'ok' to %s", ip)
        self.sock.sendto(("ok: "+str(ip)).encode(), ip)

    def listen_clients(self):
        while True:
            msg, client = self.sock.recvfrom(1024)
            logging.info('Received data from client %s: %s', client, msg.decode())
            t = threading.Thread(target=self.talkToClient, args=(client,))
            t.start()

if __name__ == '__main__':
    # Make sure all log messages show up
    logging.getLogger().setLevel(logging.DEBUG)

    b = Broker()
    b.listen_clients()