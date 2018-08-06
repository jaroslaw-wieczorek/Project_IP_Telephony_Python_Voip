import os
import sys

from threading import Thread

from functools import partial


from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QMessageBox
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
        self.username = None
        self.client = None

        self.mainWindow = None
        self.loginWindow = None
        self.registerWindow = None
        self.interactionWindow = None
        self.passwordChangeWindow = None


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
    def registerMessageResponse(self, value):
        if value:
            print("[*]  RegisterDialog info: The registerMessageResponse works")
            self.registerWindow.hide()
            print("[*]  RegisterDialog info: Register window hidden")
            self.loginWindow.show()
        else:
            self.registerWindow.showRegisterStatus("Status rejestracji | " + str(self.client.received))

    @pyqtSlot(QEvent)
    def closingSignalResponse(self, event):
        title = 'Uwaga!'
        text = 'Czy napewno chesz zamknąć aplikacje ?'

        if QMessageBox.question(self.mainWindow, title,
                                text) == QMessageBox.Yes:

            print("[*]  MyApp info: Selected answer = \'Yes\'")
            event.accept()
            self.client.closeConnection()
            self.closeAllWindows()
            print("[*]  MyApp info: The closingSignal was emitted with True")
        else:
            print("[*]  MyApp info: Selected answer = \'No\'")

            event.ignore()
            print("[*]  MyApp info: The closingSignal was emitted with False")

    @pyqtSlot(bool, str)
    def getCallSignalResponse(self, value, username):
        if value:
            print("(*) MyApp getCallSignalResponse received:", value)
            self.interactionWindow.setupCallerName(username)
            self.showInteractionWindow()
        else:
            print("(*) MyApp getCallSignalResponse received:", value)

    @pyqtSlot(bool, int)
    def activationSignalResponse(self, value, code):
        if value:
            if code == 200:
                print("(*) MyApp showActivationWindow received:", value)
                self.showActivationWindow()
                self.hideLoginWindow()
                # to do show activation window, close registe/login window


    @pyqtSlot(bool, str, list)
    def callSignalResponse(self, value, username):
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

    @pyqtSlot(bool)
    def endCallResponseResponse(self, value):
        if value:
            print("w endCallResponseResponse")
            self.interactionWindow.hide()
            self.mainWindow.showConnectionStatus("Połączenie zakończono")
            self.client.end_connection()

    @pyqtSlot(bool, list)
    def changedUsersStatusResponse(self, value, users_list):
        if value:
            if(self.client.last_list_users != users_list):
                self.mainWindow.delete_rows_users()
                self.mainWindow.add_row_to_list_of_users(users_list)
                self.client.last_list_users = users_list

    @pyqtSlot(bool)
    def endCallResponse(self, value):
        if value:
            print("w endCallResponse")
            self.interactionWindow.hide()
            self.mainWindow.showConnectionStatus("Połączenie zakończono")
            self.client.end_connection()

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
        self.interactionWindow.is_connection_begin = True
        self.interactionWindow.push_button_accept.setEnabled(False)

    # Activation Dialog methods
    def setupActivationWindow(self, activation_window):
        self.activation_window = activation_window

    def hideActivationWindow(self):
        self.activation_window.hide()

    def showActivationWindow(self):
        self.activation_window.show()
