import os
import sys
import json

import hashlib

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QEventLoop

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..'))
sys.path.append(lib_path2)

from JaroEliCall.src.test2 import ServerThread
from JaroEliCall.src.test2 import ClientThread

from JaroEliCall.src.client import Client
from JaroEliCall.src.wrapped_interfaces.activation_wrapped_ui import PasswordChangeWrappedUI


# remoteClientIP = '127.0.0.1'

class PasswdEqualError(ValueError):
    pass

class PasswdLengthError(ValueError):
    pass

class PasswordChangeDialog(PasswordChangeWrappedUI):
    # Signal used when user close app after clicked esc or cros to close app.
    # If user clicked Yes on message box return True other way return False.

    closingSignal = pyqtSignal(QEvent)

    callSignal = pyqtSignal(bool)

    def __init__(self, client):
        super(PasswordChangeDialog, self).__init__()

        self.client = client
        # self.__session_id = None

        self.loop = QEventLoop()
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.loop.exit(1))

        self.set_change_password_button(self.change_password)



    def validatePasswords(self, password, repeat_password):
        # TO DO
        if len(password) < 8:
            raise PasswdLengthError("Passwords is too short")
            return False

        if len(password) > 20:
            raise PasswdLengthError("Passwords is too long")
            return False

        if password != repeat_password:
            raise PasswdEqualError("Passwords are not equal")
            return False

        return True

    def validateLogin(self, login):
        # TO DO and CHECK
        if login is None or login == "":
            raise TypeError("Login is empty!")
            return False

        if type(login) != str:
            raise TypeError("Login is not text!")
            return False

        return True

    def validateData(self, login, password, repeat_password):

        try:
            if self.validateLogin(login):

                if self.validatePasswords(password, repeat_password):
                    return True

        except Exception as e:
            # TO DO SHOW PASSWORD CHANGE STATUS

            #self.showRegisterStatus(str(e.args[0]))
            return False

    def getActivationStatus(self):
        print("[*] ActivationDialog info: Get response from server ",
              self.client.received)

        if self.client.received == "200 CHANGED":
            status = "Status zmiany hasła | " + str(self.client.received)
            self.showRegisterStatus(status)
            return True

        elif self.client.received == "406 NOT CHANGED":
            status = "Status zmiany hasła | " + str(self.client.received)
            self.showRegisterStatus(status)
            return False

    def change_password(self):
        login = self.get_login()

        passwd = self.get_password_activate()
        passwd_hash = hashlib.sha256(passwd.encode()).hexdigest()
        repeat_passwd = self.get_repeat_password_activate()

        if self.validateData(login, passwd, repeat_passwd):

            payload = {
                "type": "d",
                "description": "CHANGE",
                "NICKNAME": login,
                "PASSWORD": passwd_hash
            }

            self.client.sendMessage(json.dumps(payload).encode("utf-8"))

            return self.getActivationStatus()
        else:
            return False

    def closeApp(self, event):
        print(event)
        self.close()

    def closeEvent(self, event):
        self.closingSignal.emit(event)

    def setUserName(self, user_name):
        self.username = user_name



    def waiting_for_signal(self):
        self.timer.start(10000)  # 10 second time-out

        print('{*} MainWindow info:  waiting for response')

        if self.loop.exec_() == 0:
            self.timer.stop()
            print("{*} MainWindow info: stop timer")
            return True
        else:
            print('{!} MainWindow error: time-out :(')
            return False



    def keyPressEvent(self, event):
        """
            Close application from escape key.
        """
        if event.key() == Qt.Key_Escape:
            self.close()
