import os
import sys
from random import randint
from threading import Thread

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)


from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


from JaroEliCall.src.functionality.login_dialog import LoginDialog
from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
from JaroEliCall.src.functionality.register_dialog import RegisterDialog
from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog




from JaroEliCall.src.client import Client
from JaroEliCall.src.class_between_threads import ClassBetweenThreads

SERWER_IP = '127.0.0.1'
PORT = 50001



class MyApp(QApplication):
    
    def setupAppWindow(self, window):
        self.mainwindow = window
    

def main():
    app : QApplication = MyApp(sys.argv) 
    client = Client(SERWER_IP, PORT)
    #toThread = betweenTherads.ClassBetweenhreads()

    logwindow = LoginDialog(client, toThread)
    """
    self.login = ''
    self.c = client
    self.toThread = toThread
    """
    logwindow.show()

   


    sys.exit(app.exec_())



if __name__ == "__main__":
    main()

