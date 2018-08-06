import os
import sys
import json

from functools import partial
from PyQt5 import QtCore

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QMessageBox

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..'))
sys.path.append(lib_path2)

from JaroEliCall.src.test2 import ServerThread
from JaroEliCall.src.test2 import ClientThread

from JaroEliCall.src.client import Client
from JaroEliCall.src.wrapped_interfaces.activation_wrapped_ui import PasswordChangeWrappedUI


# remoteClientIP = '127.0.0.1'

class ActivationWindowDialog(PasswordChangeWrappedUI):
    # Signal used when user close app after clicked esc or cros to close app.
    # If user clicked Yes on message box return True other way return False.

    closingSignal = pyqtSignal(QEvent)

    callSignal = pyqtSignal(bool)

    def __init__(self, client):
        super(ActivationWindowDialog, self).__init__()

        self.client = client
        # self.__session_id = None

        self.loop = QEventLoop()
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.loop.exit(1))

        self.set_change_password_button(self.change_password)

    def change_password(self):
        print("Changed password")

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
