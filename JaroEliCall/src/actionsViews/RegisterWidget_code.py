
import os
import sys
import json

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)


from src.interface_management.register import RegisterDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
import hashlib
from JaroEliCall.src.client import Client
import JaroEliCall.src.ClassBetweenThreads as betweenTherads
from validate_email import validate_email

#####   TO DO ####
"""     Register Widget
    Screen to Register
    register - on_reg_button_clicked = 
            * fulfilling gaps with data            
"""
#

SERWER_IP = "192.168.0.102"


class RegisterWidget(RegisterDialog):
    def __init__(self, client, login):
        super(RegisterWidget, self).__init__()
        self.client = client
        self.login = login
        self.login.hide()

        self.set_push_button_register(self.on_register_button_clicked)
        self.set_push_button_login(self.on_login_button_clicked)

    def read(self):
        print("Odczytalem ", self.toThreaad.received)
        if(self.toThreaad.received[0] == "201 CREATED"):
            print("Udało sie zarejestrować")
            self.close()
            self.login.show()
        elif(self.toThreaad.received[0] =="406 NOT_CREATED"):
            print("Nie udało sie zarejestrować")


    @pyqtSlot()
    def on_login_button_clicked(self):
        pass

    @pyqtSlot()
    def on_register_button_clicked(self):
        login = self.get_login()
        email = self.get_email()
        passw = self.get_password()
        repeat_passw = self.get_repeat_password()

       # sprawdzenie czy
        # 1 hasła są takie same,
        # 2 czy email jest poprawny,
        # 3 czy hasło jest dłuższe niż 8 znaków
        if(passw == repeat_passw and validate_email(email) and len(passw) > 8):
            passw = hashlib.sha256(passw.encode()).hexdigest()
            payload = {"type": "d", "description": "CREATE", "NICKNAME": login, "PASSWORD": passw, "EMAIL": email}
            self.client.sendMessage(json.dumps(payload).encode("utf-8"))
            self.toThreaad = betweenTherads.ClassBetweenhreads()
            with self.toThreaad.lock:
                self.client.listening(self.toThreaad)
                self.read()
        else:
            print("TO DO labele w formularzu")







