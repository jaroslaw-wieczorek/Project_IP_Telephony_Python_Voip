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


    def showLoginStatus(self, status):
        #self.addWidget(self.statusBar)
        self.statusBar.showMessage(status)
        
        
    def getLoggingStatus(self):
        print("[*] LoginDialog info: Get response from server ", self.toThread.received)
        if self.toThread.received == "200 LOGIN":
            status = "Status logowania |" + str(self.toThread.received)
            self.showLoginStatus(status)
            return True
            
        elif self.toThread.received =="406 LOGIN":
            status = "Status logowania | " + str(self.toThread.received)
            self.showLoginStatus(status)
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
                self.loggingSignal.emit(True, self.get_login())
                #self.loggedSignal.emit({"abc": 123}, name="loggedSignal" )
                print("[*] LoginDialog info: The loggingSignal was emitted with True")
          
            else:
                print("[*] LoginDialog info: The loggingToServer method returned False")
                self.loggingSignal.emit(False, self.get_login())
                print("[*] LoginDialog info: The loggingSignal was emitted with False")

        else:
            print("[*] LoginDialog info: The validateData method returned False")
            self.loggingSignal.emit(False, "")
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
            
            
