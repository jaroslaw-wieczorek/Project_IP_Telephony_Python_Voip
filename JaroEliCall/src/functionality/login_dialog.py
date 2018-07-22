import os
import sys
import json
import time
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
    loggingSignal = QtCore.pyqtSignal(bool, str)
    registerAccountSignal = QtCore.pyqtSignal(bool)

    def __init__(self, client):
        super(LoginDialog, self).__init__()
        
        self.client : Client = client
                
        self.set_push_button_login(self.clickOnLoginButton)
        self.set_push_button_register(self.clickOnRegisterButton)

        #self.closeEvent = self.closeApp
        self.loop = QtCore.QEventLoop()
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.loop.exit(1))
        
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
        #time.sleep(5)
        print("[*] LoginDialog info: Get response from server ", self.client.toThread.received)
        if self.client.toThread.received == "200 LOGIN":
            status = "Status logowania |" + str(self.client.toThread.received)
            self.showLoginStatus(status)
            return True
            
        elif self.client.toThread.received =="406 LOGIN":
            status = "Status logowania | " + str(self.client.toThread.received)
            self.showLoginStatus(status)
            return False
    
    

    def waiting_for_signal(self):
      
        self.timer.start(10000) # 10 second time-out
        
        print('fetching request...')
        if self.loop.exec_() == 0:
            self.timer.stop()
            print("Timer stop - get message")
            return self.getLoggingStatus()
        else:
            print('request timed-out :(')
    

            
    def loggingToServer(self, login, password):
        print("[*] LoginDialog info: Trying to log in to the server.", self.client.toThread.received)
        
        self.client.login(login, password)
        self.waiting_for_signal()
        
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
            
            
