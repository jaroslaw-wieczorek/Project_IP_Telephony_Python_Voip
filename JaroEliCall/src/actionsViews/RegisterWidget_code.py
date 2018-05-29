from PyQt5.QtWidgets import QDialog
from JaroEliCall.gui.register_ui import Ui_RegisterForm
from PyQt5.QtCore import pyqtSlot
import hashlib
from JaroEliCall.src.client import Client
#####   TO DO ####
"""     Register Widget
    Screen to Register
    register - on_reg_button_clicked = 
            * fulfilling gaps with data            
"""


class RegisterWidget(QDialog, Ui_RegisterForm):
    def __init__(self, client):
        super(RegisterWidget, self).__init__()
        self.setupUi(self)
        self.client = client
        self.pushButton.clicked.connect(self.on_register_button_clicked)

    @pyqtSlot()
    def on_register_button_clicked(self):
        login = self.lineEdit_6.text()
        email = self.lineEdit_8.text()
        password = self.lineEdit_7.text()
        repeat_pass = self.lineEdit_5.text()


        if(password == repeat_pass):
            passw = hashlib.sha256(password.encode()).hexdigest()
            self.client.connectToSerwer("192.168.0.103")
            ans = self.client.sendMessage(("d 0x3 CREATE " + email + " " + login + " " + passw).encode("utf-8"))
            print(ans)
            if(ans):
                self.close()
                print("uzytkownik zarejestrowany")
            else:
                print("Użytkownik o podanym loginie istnieje")
        else:
            pass




