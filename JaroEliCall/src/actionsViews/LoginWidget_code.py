from PyQt5.QtWidgets import QDialog
from JaroEliCall.gui.loging_ui import Ui_LoginForm
from JaroEliCall.src.client import Client

import os
import sys
import json

import hashlib
from threading import Thread

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)



from interface_management.login import LoginDialog


from JaroEliCall.src.client import Client

from JaroEliCall.src.actionsViews.RegisterWidget_code import RegisterWidget


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

SERWER_IP = "192.168.43.130"

class LoginWidget(LoginDialog):
    def __init__(self):
        super(LoginWidget, self).__init__()
        """
        priv = 'rsa_keys/private'
        publ = 'rsa_keys/key.pub'
        """
        self.c = Client()
        
        self.set_push_button_login(self.on_login_button_clicked)
        self.set_push_button_register(self.on_register_button_clicked)

    @pyqtSlot()
    def on_login_button_clicked(self):

        login = self.get_login()
        password = self.get_password()
        password = hashlib.sha256(password.encode()).hexdigest()
        self.c.connectToSerwer(SERWER_IP)
        print("Laczenie sie z serwerem")

        self.thread = Thread(target=self.c.listening, args=[])
        self.thread.start()

        self.c.login(login, password)


    @pyqtSlot()
    def on_register_button_clicked(self):
        # self.close()
        reg = RegisterWidget(self.c)
        reg.show()
        reg.exec_()