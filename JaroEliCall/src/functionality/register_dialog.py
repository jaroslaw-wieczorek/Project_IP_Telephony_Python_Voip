import os
import sys
import json
import hashlib

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog

from JaroEliCall.src.client import Client

from JaroEliCall.src.class_between_threads import ClassBetweenThreads
from JaroEliCall.src.wrapped_interfaces.register_wrapped_ui import RegisterWrappedUI




#from validate_email import validate_email

class RegisterDialog(RegisterWrappedUI):
    
    # Signal used when user register new account after clicked on push_button_register.
    # Return true or false. 
    # The "False" value is always emitted if the Server does not confirm the account registration.  
    registrationSignal = pyqtSignal(bool)
    
    # Signal used for return user to login window after push_button_already_account.
    # This the signal always emit value equal True.
    alreadyAccountSignal = QtCore.pyqtSignal(bool)
   
    
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__()
        
        self.set_push_button_register(self.clickOnRegisterButton)
        self.set_push_button_already_account(self.clickOnAlreadyAccountButton)
        
        
    def serverResponse(self):
        #TODO
        return True
        
    
   
    def clickOnRegisterButton(self):
        print("[*] RegisterDialog info: push_button_register was clicked")
        if self.serverResponse():
            self.registrationSignal.emit(True)
            print("[*] RegisterDialog info: registrationSignal was emitted with True")
        else:
            self.registrationSignal.emit(False)
            print("[*] RegisterDialog info: registrationSignal was emitted with False")
            
    
    def clickOnAlreadyAccountButton(self):
        print("[*] RegisterDialog info: push_button_already_account was clicked")
        self.alreadyAccountSignal.emit(True)

        
        
#####   TO DO ####
"""     Register Widget
    Screen to Register
    register - on_reg_button_clicked = 
            * fulfilling gaps with data            


class RegisterDialog(RegisterWrappedUI):
    def __init__(self, client, login):
        super(RegisterDialog, self).__init__()
        self.client = client
        self.login = login
        self.login.hide()

        self.set_push_button_register(self.on_register_button_clicked)
        self.set_push_button_login(self.on_login_button_clicked)

    def read(self):
        print("Odczytalem ", self.toThread.received)
        if(self.toThread.received[0] == "201 CREATED"):
            print("Udało sie zarejestrować")
            self.close()
            self.login.show()
        elif(self.toThread.received[0] =="406 NOT_CREATED"):
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
            self.toThread = ClassBetweenhreads()
            with self.toThread.lock:
                self.client.listening(self.toThread)
                self.read()
        else:
            print("TO DO labele w formularzu")

"""





