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
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QMessageBox

from JaroEliCall.src.client import Client
from JaroEliCall.src.functionality.my_app import *
from JaroEliCall.src.functionality.signal import Signal
from JaroEliCall.src.wrapped_interfaces.login_wrapped_ui import LoginWrappedUI


class LoginDialog(LoginWrappedUI):

    """
       New LoginDialog
    """

    closingSignal = pyqtSignal(QEvent)
    loggingSignal = QtCore.pyqtSignal(bool, str)
    registerAccountSignal = QtCore.pyqtSignal(bool)



    def __init__(self, client):
        super(LoginDialog, self).__init__()

        self.client : Client = client

        self.set_push_button_login(self.clickOnLoginButton)
        self.set_push_button_register(self.clickOnRegisterButton)
        self.closingSignal.connect(self.closingSignalResponse)

        #self.closeEvent = self.closeApp
        self.loop = QtCore.QEventLoop()
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.loop.exit(1))
        
        #self.closeEvent = self.closeEvent
        
        
    def validateData(self):
        # TO DO
        return True


    def showLoginStatus(self, status):
        #self.addWidget(self.statusBar)
        self.statusBar.showMessage(status)


    def getLoggingStatus(self):
        #time.sleep(5)
        print("[*] LoginDialog info:  from server", self.client.received)
        if self.client.received == "200 LOGIN":
            status = "Status logowania |" + str(self.client.received)
            #print(status)
            self.showLoginStatus(status)
            return True

        elif self.client.received == "406 LOGIN":
            status = "Status logowania | " + str(self.client.received)
            #print(status)
            self.showLoginStatus(status)
            return False



    def waiting_for_signal(self):

        self.timer.start(10000) # 1 second time-out

        print('[*] LoginDialog info: waiting for response')

        if self.loop.exec_() == 0:
            self.timer.stop()
            print("[*] LoginDialog info: stop timer")
            return True
        else:
            print('[!] LoginDialog error: timed-out')
            return False


    def loggingToServer(self, login, password):

        self.client.login(login, password)
        if self.waiting_for_signal():
            return self.getLoggingStatus()
        else:
            return False


    def clickOnLoginButton(self):
        print("[*] LoginDialog info: The push_button_login was clicked")

        if self.validateData:
            print("[*] LoginDialog info: The validateData method returned True")
            #print("[*] Answer loggingToServer ", self.loggingToServer(self.get_login(), self.get_password()))

            if self.loggingToServer(self.get_login(), self.get_password()):
                print("[*] LoginDialog info: The loggingToServer method returned True")
                self.loggingSignal.emit(True, self.get_login())
                # self.loggedSignal.emit({"abc": 123}, name="loggedSignal")
                print("[*] LoginDialog info: The loggingSignal was emitted with True")

            else:
                print("[*] LoginDialog info: The loggingToServer method returned False")
                self.loggingSignal.emit(False, self.get_login())
                print("[*] LoginDialog info: The loggingSignal was emitted with False")

        else:
            print("[*] LoginDialog error: The validateData method returned False")
            self.loggingSignal.emit(False, "")
            print("[*] LoginDialog info: The loggingSignal was emitted with False")


    def clickOnRegisterButton(self):
        print("[*] LoginDialog info: The push_button_register was clicked")
        self.registerAccountSignal.emit(True)
        print("[*] LoginDialog info: The registerAccountSignal was emitted with True")


    def closeEvent(self, event):
        self.closingSignal.emit(event)
        
        
    def closeApp(self, event):
        print(event)
        self.close()
        

    def keyPressEvent(self, event):
        """
            Close application from escape key.
        """
        if event.key() == Qt.Key_Escape:
            self.close()
            
    
    @pyqtSlot(QEvent)
    def closingSignalResponse(self, event):

        if QMessageBox.question(self, 'Uwaga!', 'Czy napewno chesz zamknąć aplikacje ?') == QMessageBox.Yes:
            print("[*]  LoginDialog info: Selected answer = \'Yes\'")
            event.accept()
            #self.client.closeConnection()
            self.client.socket.close()
            print("[*]  LoginDialog info: The QCloseEvent accept")
        else:
            print("[*]  LoginDialog info: Selected answer = \'No\'")
            #self.closingSignal.emit(False)
            event.ignore()
            print("[*]  LoginDialog info: The QCloseEvent ignore")

