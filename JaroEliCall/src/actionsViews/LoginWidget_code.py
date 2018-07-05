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
from JaroEliCall.gui.loging_ui import Ui_LoginForm

from JaroEliCall.src.ClassBetweenThreads import ClassBetweenhreads
from JaroEliCall.src.actionsViews.AdduserWidget_code import AddUserWidget
from JaroEliCall.src.actionsViews.RegisterWidget_code import RegisterWidget
from JaroEliCall.src.interface_management.login import LoginDialog


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


class LoginWidget(LoginDialog):

    def __init__(self, client, toThread):
        super(LoginWidget, self).__init__()
        """
        priv = 'rsa_keys/private'
        publ = 'rsa_keys/key.pub'
        """
        self.login = ''
        self.c = client
        self.toThread = toThread
        self.set_push_button_login(self.on_login_button_clicked)
        self.set_push_button_register(self.on_register_button_clicked)


    def read(self):
        print("Odczytalem ", self.toThread.received)
        if(self.toThread.received[0] == "200 LOGIN"):
            self.close()

        elif(self.toThread.received[0] =="406 LOGIN"):
            print("TO DO label z Nieprawidłowe dane ")


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
        reg = RegisterWidget(self.c, self)
        reg.show()
        reg.exec_()