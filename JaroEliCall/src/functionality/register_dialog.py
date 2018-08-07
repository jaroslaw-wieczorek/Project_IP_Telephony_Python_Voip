import os
import re
import sys
import json
import hashlib

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path2)

from JaroEliCall.src.client import Client
from JaroEliCall.src.wrapped_interfaces.register_wrapped_ui import RegisterWrappedUI


class LoginLengthError(ValueError):
    pass


class EmailValidError(ValueError):
    pass


class RegisterDialog(RegisterWrappedUI):

    # Signal used when user register new account after clicked
    # on push_button_register. Return true or false.
    # The "False" value is always emitted if the Server
    # does not confirm the account registration.
    registrationSignal = pyqtSignal(bool)

    # Signal used for return user to login window
    # after push_button_already_account.
    # This the signal always emit value equal True.
    alreadyAccountSignal = pyqtSignal(bool)

    # Close signal
    closingSignal = pyqtSignal(QEvent)

    def __init__(self, client):
        super(RegisterDialog, self).__init__()

        self.client = client

        self.set_push_button_register(self.clickOnRegisterButton)
        self.set_push_button_already_account(self.clickOnAlreadyAccountButton)
        self.closingSignal.connect(self.closingSignalResponse)

        self.line_edit_password.hide()
        self.label_password.hide()
        self.line_edit_repeat_password.hide()
        self.label_repeat_password.hide()
        # self.closeEvent = self.closeEvent

    def validateLogin(self, login):
        # TO DO and CHECK
        if login is None or login == "":
            raise TypeError("Login is empty!")
            return False

        if type(login) != str:
            raise TypeError("Login is not text!")
            return False

        return True

    def validate_email(self, email):
        regex = r"""^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"""
        result = False
        if re.match(regex, email):
            result = True


        print("result", result)

        # print("email_exist", email_exists)
        # if result is True and email_exists is False:
        if result is True:
            return True
        else:
            return False

    def validateEmail(self, email):
        if self.validate_email(email):
            return True
        else:
            raise EmailValidError("Email is not correct!")
            return False



    def validateData(self, login, email):

        try:
            if self.validateLogin(login):

                if self.validateEmail(email):

                    return True

        except Exception as e:
            self.showRegisterStatus(str(e.args[0]))
            return False

    def showRegisterStatus(self, status):
        # self.addWidget(self.statusBar)
        self.statusBar.showMessage(status)

    def getRegisterStatus(self):
        print("[*] RegisterDialog info: Get response from server ",
              self.client.received)

        if self.client.received == "201 CREATED":
            status = "Status rejestracji | " + str(self.client.received)
            self.showRegisterStatus(status)
            return True

        elif self.client.received == "406 NOT_CREATED":
            status = "Status rejestracji | " + str(self.client.received)
            self.showRegisterStatus(status)
            return False

    def registerAccount(self):
        login = self.get_login()
        email = self.get_email()

        if self.validateData(login,email):

            payload = {
                        "type": "d",
                        "description": "CREATE",
                        "NICKNAME": login,
                        "EMAIL": email
                        }

            self.client.sendMessage(json.dumps(payload).encode("utf-8"))

            return self.getRegisterStatus()
        else:
            return False

    def clickOnRegisterButton(self):
        print("[*] RegisterDialog info: push_button_register was clicked")
        if self.registerAccount():
            self.registrationSignal.emit(True)
            print("[*] RegisterDialog info: registrationSignal " +
                  "was emitted with True")
        else:
            self.registrationSignal.emit(False)
            print("[*] RegisterDialog info: registrationSignal " +
                  "was emitted with False")

    def clickOnAlreadyAccountButton(self):
        print("[*] RegisterDialog info: push_button_already_account " +
              " was clicked")
        self.alreadyAccountSignal.emit(True)

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
