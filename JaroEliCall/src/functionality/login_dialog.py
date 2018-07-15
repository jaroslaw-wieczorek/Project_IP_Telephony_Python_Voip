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
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QMessageBox

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
    closingSignal = pyqtSignal(bool)
    loggingSignal = QtCore.pyqtSignal(bool)
    registerAccountSignal = QtCore.pyqtSignal(bool)

    def __init__(self, client, toThread):
        super(LoginDialog, self).__init__()
        
        self.client = client
        self.toThread = toThread
        
        self.set_push_button_login(self.clickOnLoginButton)
        self.set_push_button_register(self.clickOnRegisterButton)

        #self.closeEvent = self.closeApp
        
    def keyPressEvent(self, event):
        """
            Close application from escape key.
        """
        if event.key() == QtCore.Qt.Key_Escape:
            self.closeApp()


    def validateData(self):
        # TO DO 
        return True


    def showLoginStatus(self, value):
        #self.addWidget(self.statusBar)
        self.statusBar.showMessage("Błąd podczas logowania")
        
        
    def getLoggingStatus(self):
        print("[*] LoginDialog info: Get response from server ", self.toThread.received)
        if self.toThread.received == "200 LOGIN":
            return True
            
        elif self.toThread.received =="406 LOGIN":
            return False
        

    def loggingToServer(self, login, password):
        print("[*] LoginDialog info: Trying to log in to the server.", self.toThread.received)
        self.client.login(login, password)
        
        with self.toThread.lock:
            self.client.listening(self.toThread)
            return self.getLoggingStatus()


    def clickOnLoginButton(self):
        print("[*] LoginDialog info: The push_button_login was clicked")
          
        if self.validateData:
            print("[*] LoginDialog info: The validateData method returned True")
            
            if self.loggingToServer(self.get_login(), self.get_password()):
                print("[*] LoginDialog info: The loggingToServer method returned True")
                self.loggingSignal.emit(True)
                #self.loggedSignal.emit({"abc": 123}, name="loggedSignal" )
                print("[*] LoginDialog info: The loggingSignal was emitted with True")
          
            else:
                print("[*] LoginDialog info: The loggingToServer method returned False")
                self.loggingSignal.emit(False)
                print("[*] LoginDialog info: The loggingSignal was emitted with False")

        else:
            print("[*] LoginDialog info: The validateData method returned False")
            self.loggingSignal.emit(False)
            print("[*] LoginDialog info: The loggingSignal was emitted with False")


    def clickOnRegisterButton(self):
        print("[*] LoginDialog info: The push_button_register was clicked")
        self.registerAccountSignal.emit(True)
        print("[*] LoginDialog info: The registerAccountSignal was emitted with True")
        
    
    def closeApp(self):
        title = "Uwaga!"
        message = "Czy napewno chesz zamknąć aplikacje ?"
        
        if QMessageBox.question(self, title, message) == QMessageBox.Yes:
            print("[*]  LoginDialog info: Selected answer = \'Yes\'")
            self.closingSignal.emit(True) 
            print("[*]  LoginDialog info: The closingSignal was emitted with True")
        else:
            print("[*]  LoginDialog info: Selected answer = \'No\'")
            self.closingSignal.emit(False)
            print("[*]  LoginDialog info: The closingSignal was emitted with False")
            
            
            
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

"""

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