
import os
import sys
import json

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

from src.interface_management.register import RegisterDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
import hashlib
from JaroEliCall.src.client import Client


#####   TO DO ####
"""     Register Widget
    Screen to Register
    register - on_reg_button_clicked = 
            * fulfilling gaps with data            
"""
#
SERWER_IP = "192.168.0.103"

class RegisterWidget(RegisterDialog):
    def __init__(self, client):
        super(RegisterWidget, self).__init__()
         self.client = client
        

    @pyqtSlot()
    def on_register_button_clicked(self):
        login = self.get_login()
        email = self.get_email()
        passw = self.get_password()
        repeat_passw = self.get_repeat_password()


        if(passw == repeat_passw):
            passw = hashlib.sha256(passw.encode()).hexdigest()
            self.client.connectToSerwer(SERWER_IP)
            ans = self.client.sendMessage(("d 0x3 CREATE " + email + " " + login + " " + passw).encode("utf-8"))
            print(ans)
            if(ans):
                self.close()
                print("uzytkownik zarejestrowany")
            else:
                print("uzytkownik o podanym loginie istnieje")
        else:
            pass




