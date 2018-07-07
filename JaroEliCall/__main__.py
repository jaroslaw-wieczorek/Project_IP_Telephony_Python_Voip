import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QAction
from .gui.main_ui import Ui_MainWindow
from .gui.settings_ui import Ui_SettingsDialog


from JaroEliCall.src.actionsViews.LoginWidget_code import LoginWidget
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
    
    def setup_client(self, client : Client):
        self._client = Client
    
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
      
        self.actSettings.triggered.connect(self.showSettings)
        
    def showSettings(self):
        self.s = Dialog(QDialog())
        self.s.setupUi(self.s)
        self.s.show()

        
        
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

