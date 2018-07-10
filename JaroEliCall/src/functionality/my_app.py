import os
import sys

from functools import partial

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication


src_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(src_path)

from JaroEliCall.src.functionality.signal import Signal
#from JaroEliCall.src.functionality.login_dialog import LoginDialog
# from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
# from JaroEliCall.src.functionality.register_dialog import RegisterDialog
# from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog


   
class MyApp(QApplication):

    procDone = QtCore.pyqtSignal(bool)
    
    def __init__(self, *agrs, **kwargs):
        super(MyApp, self).__init__(*agrs, **kwargs)
        
        self.mainWindow = None
        self.loginWindow = None
        self.registerWindow = None
        
    # MainWindow Dialog methods
    def setupMainWindow(self, main_window):
        self.mainWindow = main_window
       
#    @staticmethod
        
    @QtCore.pyqtSlot(bool)
    def on_procStart(self, value):
        print(value)
        if value:
            self.hideLoginWindow()
        else:
            print("get: ", value)
            
       # self.raise_()
        
      
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
