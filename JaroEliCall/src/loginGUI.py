from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
import client
import hashlib
import socket


class loginGUI(QDialog):
    def __init__(self):
        super(loginGUI, self).__init__()
        loadUi('login.ui', self)
        self.setWindowTitle('JaroEliCall')
        self.login_button.clicked.connect(self.on_login_Button_clicked)

    @pyqtSlot()
    def on_login_Button_clicked(self):
        priv = 'rsa_keys/private'
        publ = 'rsa_keys/key.pub'

        print(socket.gethostbyname(socket.gethostname()))

        login, password = self.login_VALUE.text(), self.password_VALUE.text()
        password = hashlib.sha256(password.encode()).hexdigest()

        self.c = client.Client(priv, publ)
        self.c.connectToSerwer()
        self.c.login(login, password)



app = QApplication(sys.argv)
widget = loginGUI()
widget.show()
sys.exit(app.exec_())