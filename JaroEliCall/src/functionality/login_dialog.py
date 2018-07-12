import os
import sys
import json
import hashlib
import threading
from functools import partial



lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

print(lib_path)
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)


from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog

from JaroEliCall.src.client import Client
from src.functionality.my_app import *
from JaroEliCall.src.functionality.signal import Signal
from JaroEliCall.src.class_between_threads import ClassBetweenThreads
from JaroEliCall.src.wrapped_interfaces.login_wrapped_ui import LoginWrappedUI


class LoginDialog(LoginWrappedUI):
   
    """
        New LoginDialog
    """
    #test
    loggingSignal = QtCore.pyqtSignal(bool)
    registerAccountSignal = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(LoginDialog, self).__init__()
        
        self.set_push_button_login(self.clickOnLoginButton)
        self.set_push_button_register(self.clickOnRegisterButton)


    def loginStatus(self, value):
        return(value)


    def serverResponse(self):
        #TODO
        return True


   #@QtCore.pyqtSlot(bool)
    def clickOnLoginButton(self):
        print("[*] LoginDialog info: push_button_login was clicked")
    
        if self.serverResponse():
            self.loggingSignal.emit(True)
            
            #self.loggedSignal.emit({"abc": 123}, name="loggedSignal" )
            print("[*] LoginDialog info: loggingSignal was emitted with True")
        else:
            self.loggingSignal.emit(False)
        
            print("[*] LoginDialog info: loggingSignal was emitted with False")


    #@QtCore.pyqtSlot(bool)
    def clickOnRegisterButton(self):
        print("[*] LoginDialog info: push_button_register was clicked")
        self.registerAccountSignal.emit(True)
        print("[*] LoginDialog info: registerAccountSignal was emitted with True")
        
    
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

class LoginDialog(LoginWrappedUI):
    
     #This class is implementation of Login dialog with all functionality like 
     #send and recive data for login users.
     
     #Constructor take 2 arguments used to create this widget:
     #    First from them is Client object used to communicate between Server and App.
     #    Secound is parent object 
     
    
    

    def __init__(self, client, toThread):
        super(LoginDialog, self).__init__()
        
        self.toThread = toThread
       
    

        self.set_push_button_login(self.on_login_button_clicked)
        self.set_push_button_register(self.on_register_button_clicked)


    def read(self):
        print("Odczytalem ", self.toThread.received)
        if(self.toThread.received[0] == "200 LOGIN"):
            
            self.parent().hide()
            

        elif(self.toThread.received[0] =="406 LOGIN"):

            print("TO DO label z Nieprawidłowe dane ")


    def get_status(self):
        while (self.logging_in == ''):
            print("Czekam...")
        return self.logging_in
   
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
        pass
        #reg = RegisterWidget(self.c, self)
        #reg.show()
        #reg.exec_()
"""