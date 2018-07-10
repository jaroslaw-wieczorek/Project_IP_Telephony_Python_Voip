import os
import sys
from random import randint
from threading import Thread

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from JaroEliCall.src.functionality.signal import Signal
from JaroEliCall.src.functionality.my_app import MyApp
from JaroEliCall.src.functionality.login_dialog import LoginDialog
from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
from JaroEliCall.src.functionality.register_dialog import RegisterDialog
from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog

from JaroEliCall.src.client import Client
from JaroEliCall.src.class_between_threads import ClassBetweenThreads

SERWER_IP = '127.0.0.1'
PORT = 50001

   
def main():
    myapp = MyApp(sys.argv)

 
    #widgetB.procDone.connect(self.widgetA.on_widgetB_procDone)
    client = Client(SERWER_IP, PORT)
    toThread = ClassBetweenThreads()
    
    #window = QWidget()
    #window.resize(250, 150)
    #window.move(300,300)
    #window.setWindowTitle("Simple")
    #window.show()pomnik kanadzie
    # app.setupMainWindow = MainWindowDialog()

    loginWindow = LoginDialog()
    myapp.setupLoginWindow(loginWindow)
    
    myapp.loginWindow.procStart.connect(myapp.on_procStart)
    #myapp.procDone.connect(myapp.loginWindow.on_procDone)
    
    #myapp.loginWindow.onstart.connect(myapp.on_procStart)

    #signal = Signal()
    #signal.connect(myapp.loginWindow.loginStatus)

    myapp.showLoginWindow()

    registerWindow = RegisterDialog(parent=myapp)
    myapp.setupRegisterWindow(registerWindow)
    
    
    #toThread = betweenTherads.ClassBetweenhreads()
    
    
    """
    self.login = ''
    self.c = client
    self.toThread = toThread
    """

    
    sys.exit(myapp.exec_())



if __name__ == "__main__":
    main()

