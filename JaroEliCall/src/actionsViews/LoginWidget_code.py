from PyQt5.QtWidgets import QDialog
from JaroEliCall.gui.loging_ui import Ui_Form
from JaroEliCall.src.client import Client
import hashlib
from PyQt5.QtCore import pyqtSlot
from threading import Thread
from JaroEliCall.src.actionsViews.RegisterWidget_code import RegisterWidget
from JaroEliCall.src.actionsViews.AdduserWidget_code import AddUserWidget


"""     Login Widget
    Screen to login in and register
    login - on_login_button_clicked = 
            * creating a client with private and public key from file
            * try to log in with data from lineEdit and lineEdit2
            * if login ok going to listeners.ui screen
            * else showing a label
    register - on_register_button_clicked = 
            * goin to register.ui screen
            
"""

class LoginWidget(QDialog, Ui_Form):
    def __init__(self):
        super(LoginWidget, self).__init__()
        self.setupUi(self)
        """priv = 'rsa_keys/private'
        publ = 'rsa_keys/key.pub'"""
        self.c = Client()
        self.login_btn.clicked.connect(self.on_login_button_clicked)
        self.register_btn.clicked.connect(self.on_register_button_clicked)

    @pyqtSlot()
    def on_login_button_clicked(self):

        login, password = self.lineEdit.text(), self.lineEdit_2.text()
        password = hashlib.sha256(password.encode()).hexdigest()
        self.c.connectToSerwer('127.0.0.1')
        print("Laczenie sie z serwerem")
        answer = (self.c.login(login, password))

        print(answer, " ", login, " ", password)


        if (answer):
        # self.close()
        # przekazanie klienta miedzy widokami
            users = AddUserWidget(self.c)
            users.load_contracts()
            users.show()
            users.exec_()

    @pyqtSlot()
    def on_register_button_clicked(self):
        self.close()
        reg = RegisterWidget(self.c)
        reg.show()
        reg.exec_()







