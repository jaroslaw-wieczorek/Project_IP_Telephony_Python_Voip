import os
import sys

from functools import partial

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication


src_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(src_path)


from JaroEliCall.src.client import Client
from JaroEliCall.src.functionality.signal import Signal


#from JaroEliCall.src.functionality.login_dialog import LoginDialog
# from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
# from JaroEliCall.src.functionality.register_dialog import RegisterDialog
# from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog

SERWER_IP = '127.0.0.1'
PORT = 50001

   
class MyApp(QApplication):

    #loggingSignalResponse = QtCore.pyqtSignal(bool)
    registerSignalResponse = QtCore.pyqtSignal(bool)
    client = Client(SERWER_IP, PORT)
    
    def __init__(self, *agrs, **kwargs):
        super(MyApp, self).__init__(*agrs, **kwargs)
        
        self.mainWindow = None
        self.loginWindow = None
        self.registerWindow = None
        
    # MainWindow Dialog methods
    def setupMainWindow(self, main_window):
        self.mainWindow = main_window
       
        
    @QtCore.pyqtSlot(bool)
    def loggingSignalResponse(self, value):
        print("(*) MyApp loggingSignalResponse received:", value)
        if value:
            self.hideLoginWindow()
            self.showMainWindow()
        else:
            print("(*) MyApp loggingSignalResponse received:", value)
            # TO DO: 
            # Displays an error in the status bar that was received during
            # a failed login attempt.

            
    @QtCore.pyqtSlot(bool)
    def registerAccountSignalResponse(self, value):
        if value:
            print("(*) Myapp registerAccountSignalResponse recived:", value)
            self.hideLoginWindow()
            self.showRegisterWindow()
        else:
            print("(*) Myapp registerAccountSignalResponse recived:", value)
            # TO DO: 
            # Displays an error received during a failed registration
            # in the status bar.


    @QtCore.pyqtSlot(bool)
    def registerSignalResponse(self, value):
        if value:
            print("(*) MyApp registerSignalResponse received:", value)
            self.hideRegisterWindow()
            self.showLoginWindow()
            # TO DO:  show info about registration email in status bar.
        else:
            print("(*) MyApp registerSignalResponse received:", value)    
            
            
    @QtCore.pyqtSlot(bool)
    def alreadyAccountSignalResponse(self, value):
        if value:
            print("(*) MyApp alreadyAccountSignalResponse received:", value)
            self.hideRegisterWindow()
            self.showLoginWindow()
        else:
            print("(*) MyApp alreadyAccountSignalResponse received:", value) 
            
    
        
    def showMainWindow(self):
        self.mainWindow.show()
     
    # Login Dialog methods
    def setupLoginWindow(self, login_window):
        self.loginWindow = login_window

    def hideLoginWindow(self):
        self.loginWindow.hide()

    #@pyqtSlot(bool)
    def showLoginWindow(self):
        self.loginWindow.show()

    # Register Dialog methods
    def setupRegisterWindow(self, register_window):
        self.registerWindow = register_window


    def hideRegisterWindow(self):
        self.registerWindow.hide()


    def showRegisterWindow(self):
        self.registerWindow.show()
