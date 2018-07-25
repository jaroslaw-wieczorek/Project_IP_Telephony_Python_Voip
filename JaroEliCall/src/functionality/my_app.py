import os
import sys

from threading import Thread

from functools import partial


from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QApplication


src_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(src_path)


from JaroEliCall.src.client import Client
from JaroEliCall.src.functionality.signal import Signal


#from JaroEliCall.src.functionality.login_dialog import LoginDialog
# from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
# from JaroEliCall.src.functionality.register_dialog import RegisterDialog
# from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog


class MyApp(QApplication):


    def __init__(self, *agrs, **kwargs):
        super(MyApp, self).__init__(*agrs, **kwargs)

        self.username : str = None
        self.client : Client = None

        self.mainWindow = None
        self.loginWindow = None
        self.registerWindow = None
        self.interactionWindow = None

        self.eventClose = self.closingSignalResponse


    # Slots for communicate
    @pyqtSlot(bool, str)
    def loggingSignalResponse(self, status, login):
        if status:
            print("(*) MyApp loggingSignalResponse received:", status)
            self.hideLoginWindow()
            self.mainWindow.setUserName(login)
            self.showMainWindow()
        else:
            print("(*) MyApp loggingSignalResponse received:", status)


    @pyqtSlot(bool)
    def registerAccountSignalResponse(self, value):
        if value:
            print("(*) Myapp registerAccountSignalResponse recived:", value)
            self.hideLoginWindow()
            self.showRegisterWindow()
        else:
            print("(*) Myapp registerAccountSignalResponse recived:", value)


    @pyqtSlot(bool)
    def registerSignalResponse(self, value):
        if value:
            print("(*) MyApp registerSignalResponse received:", value)
            self.hideRegisterWindow()
            self.showLoginWindow()
            # TO DO:
            # Display an information on status bar, about sending email with
            # confirm registration link.
        else:
            print("(*) MyApp registerSignalResponse received:", value)


    @pyqtSlot(bool)
    def alreadyAccountSignalResponse(self, value):
        if value:
            print("(*) MyApp alreadyAccountSignalResponse received:", value)
            self.hideRegisterWindow()
            self.showLoginWindow()
        else:
            print("(*) MyApp alreadyAccountSignalResponse received:", value)


    @pyqtSlot(bool)
    def closingSignalResponse(self, value):
        if value:
            print("(*) MyApp closingSignalResponse received:", value)
            self.closeAllWindows()

        else:
            print("(*) MyApp closingSignalResponse received:", value)


    @pyqtSlot(bool, str)
    def getCallSignalResponse(self, value, username):
        if value:
            print("(*) MyApp getCallSignalResponse received:", value)
            self.interactionWindow.setupCallerName(username)
            self.showInteractionWindow()
        else:
            print("(*) MyApp getCallSignalResponse received:", value)

    @pyqtSlot(bool, str, list)
    def callSignalResponse(self, value, username, address):
        if value:
            print("(*) MyApp callSignalResponse received:", value)
            print(username)
            self.interactionWindow.showCallerName(username)
            self.showInteractionWindow()
            self.blockAcceptConnButton()
            print("(*) MyApp callSignalResponse shown")
        else:
            status = "Uzytkownik odrzucił połączenie"
            self.mainWindow.showConnectionStatus(status)
            print(status)
            print("(*) MyApp callSignalResponse received:", value)

    # Managment client and connection
    def setupClient(self, client):
        self.client = client
        self.listen_server_thread = Thread(
                target=self.client.listeningServer, daemon=True)
        self.listen_server_thread.start()

    # MainWindow Dialog methods
    def setupMainWindow(self, main_window):
        self.mainWindow = main_window


    def showMainWindow(self):
        self.mainWindow.show()
        self.mainWindow.getList()

    # Login Dialog methods
    def setupLoginWindow(self, login_window):
        self.loginWindow = login_window


    def hideLoginWindow(self):
        self.loginWindow.hide()


    def showLoginWindow(self):
        self.loginWindow.show()


    # Register Dialog methods
    def setupRegisterWindow(self, register_window):
        self.registerWindow = register_window


    def hideRegisterWindow(self):
        self.registerWindow.hide()


    def showRegisterWindow(self):
        self.registerWindow.show()


    # Interaction Dialog methods
    def setupInteractionWindow(self, interaction_window):
        self.interactionWindow = interaction_window


    def hideInteractionWindow(self):
        self.interactionWindow.hide()


    def showInteractionWindow(self):
        self.interactionWindow.show()
        self.interactionWindow.push_button_accept.setEnabled(True)


    def blockAcceptConnButton(self):
        self.interactionWindow.push_button_accept.setEnabled(False)


