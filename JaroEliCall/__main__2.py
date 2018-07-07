import os
import sys
from random import randint
from threading import Thread

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)

from JaroEliCall.src.app_functionality.client import Client

from JaroEliCall.src.app_functionality.login import LoginWidget
from JaroEliCall.src.actionsViews.LoginWidget_code import AddUserWidget

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from JaroEliCall.src.interface_management.settings import SettingsDialog
from JaroEliCall.src.actionsViews.MainWidget_code import MainWidget
from JaroEliCall.src.interface_management.login import LoginDialog
from JaroEliCall.src.client import Client

import JaroEliCall.src.ClassBetweenThreads as betweenTherads

SERWER_IP = '127.0.0.1'
PORT = 50001



class MyApp(QApplication):
    
    def setupApp(self):
        pass
    

def main():
    app : QApplication = MyApp(sys.argv) 
    client = Client(SERWER_IP, PORT)
    
    loginDialog = LoginDialog()
    loginDialog.show()
    
    
    #toThread = betweenTherads.ClassBetweenhreads()

    #logwindow = LoginWidget(client, toThread)
    
    #logwindow.show()
    
    
   


    sys.exit(app.exec_())



if __name__ == "__main__":
    main()

