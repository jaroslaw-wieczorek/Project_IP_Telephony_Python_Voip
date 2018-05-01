from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
import client
import hashlib
import socket
import listaGUI
from PyQt5 import uic

#load both ui file
uifile_1 = 'login.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

class loginGUI(base_1, form_1):

    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.on_login_button_clicked)
        # wchodzi mi dwa razy do pyqtslot
        self.it = 0

    @pyqtSlot()
    def on_login_button_clicked(self):
        if(self.it == 0):
            self.it = 1

            priv = 'rsa_keys/private'
            publ = 'rsa_keys/key.pub'

            print(socket.gethostbyname(socket.gethostname()))

            login, password = self.login_VALUE.text(), self.password_VALUE.text()
            password = hashlib.sha256(password.encode()).hexdigest()

            self.c = client.Client(priv, publ)
            self.c.connectToSerwer()
            ans = (self.c.login(login, password))

            if(ans == 1):
                self.main = listaGUI.listaGUI(self.c)
                self.main.show()
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = loginGUI()
    ex.show()
    sys.exit(app.exec_())

