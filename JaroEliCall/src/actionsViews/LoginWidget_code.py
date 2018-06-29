from PyQt5.QtWidgets import QDialog
from JaroEliCall.gui.loging_ui import Ui_LoginForm
from JaroEliCall.src.client import Client

import os
import sys
import json

import hashlib
from PyQt5.QtCore import pyqtSlot
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)

from JaroEliCall.src.actionsViews.AdduserWidget_code import AddUserWidget
from interface_management.login import LoginDialog
from JaroEliCall.src.client import Client
from JaroEliCall.src.actionsViews.RegisterWidget_code import RegisterWidget
import threading
import JaroEliCall.src.ClassBetweenThreads as betweenTherads


"""     Login Widget
    Screen to login in and registerS
    login - on_login_button_clicked = 
            * creating a client with private and public key from file
            * try to log in with data from lineEdit and lineEdit2
            * if login ok going to listeners.ui screen
            * else showing a label
    register - on_register_button_clicked = 
            * goin to register.ui screen            
"""


class LoginWidget(LoginDialog):
    def __init__(self, client):
        super(LoginWidget, self).__init__()
        """
        priv = 'rsa_keys/private'
        publ = 'rsa_keys/key.pub'
        """
        self.c = client
        self.set_push_button_login(self.on_login_button_clicked)
        self.set_push_button_register(self.on_register_button_clicked)

    def read(self):
        print("Odczytalem ", self.toThreaad.received)
        if(self.toThreaad.received[0] == "200 LOGIN"):
            self.close()

        elif(self.toThreaad.received[0] =="406 LOGIN"):
            print("TO DO label z Nieprawidłowe dane ")

    @pyqtSlot()
    def on_login_button_clicked(self):

        login = self.get_login()
        password = self.get_password()
        password = hashlib.sha256(password.encode()).hexdigest()
        print("Laczenie sie z serwerem")
        self.c.login(login, password)

        self.toThreaad = betweenTherads.ClassBetweenhreads()

        with self.toThreaad.lock:
            self.c.listening(self.toThreaad)
            self.read()

    @pyqtSlot()
    def on_register_button_clicked(self):
        reg = RegisterWidget(self.c, self)
        reg.show()
        reg.exec_()