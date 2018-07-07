import os
import sys
import json
import hashlib
import threading

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from JaroEliCall.src.client import Client
from JaroEliCall.src.class_between_threads import ClassBetweenThreads

from JaroEliCall.src.wrapped_interfaces.login_wrapped_ui import LoginWrappedUI


"""     
    Login Widget
    Screen to login in and registerS
    login - on_login_button_clicked = 
            * creating a client with private and public key from file
            * try to log in with data from lineEdit and lineEdit2
            * if login ok going to listeners.ui screen
            * else showing a label
    register - on_register_button_clicked = 
            * goin to register.ui screen            
"""


class LoginDialog(LoginWrappedUI):

    def __init__(self, client):
        super(LoginDialog, self).__init__()
        """
        priv = 'rsa_keys/private'
        publ = 'rsa_keys/key.pub'
        """

        self.set_push_button_login(self.on_login_button_clicked)
        self.set_push_button_register(self.on_register_button_clicked)


    def read(self):
        print("Odczytalem ", self.toThread.received)
        if(self.toThread.received[0] == "200 LOGIN"):
            self.logging_in = 200
            self.close()

        elif(self.toThread.received[0] =="406 LOGIN"):
            self.logging_in = 406
            print("TO DO label z Nieprawidłowe dane ")


    def get_status(self):
        while (self.logging_in == ''):
            print("Czekam...")
        return self.logging_in
   
    @pyqtSlot()
    def on_login_button_clicked(self):
        login = self.get_login()
        password = self.get_password()
        password = hashlib.sha256(password.encode()).hexdigest()
        
        print("Laczenie sie z serwerem")
        
        self.c.login(login, password)
        self.login = login


        with self.toThread.lock:
            self.c.listening(self.toThread)
            self.read()


    @pyqtSlot()
    def on_register_button_clicked(self):
        pass
        #reg = RegisterWidget(self.c, self)
        #reg.show()
        #reg.exec_()