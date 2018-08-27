import os
import sys
import json

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QListWidgetItem


lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..'))
sys.path.append(lib_path2)


from JaroEliCall.src.test2 import ServerThread
from JaroEliCall.src.test2 import ClientThread


from JaroEliCall.src.client import Client
from JaroEliCall.src.wrapped_interfaces.main_wrapped_ui import MainWrappedUI
from JaroEliCall.src.functionality.credits_dialog import CreditsDialog

# remoteClientIP = '127.0.0.1'

class MainWindowDialog(MainWrappedUI):

    # Signal used when user close app after clicked esc or cros to close app.
    # If user clicked Yes on message box return True other way return False.

    closingSignal = pyqtSignal(QEvent)
    callSignal = pyqtSignal(bool)
    creditsSignal = pyqtSignal(bool)

    def __init__(self, client):
        super(MainWindowDialog, self).__init__()

        self.client = client
        self.prefix = ":/avatars/"

        self.loop = QEventLoop()

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.loop.exit(1))

        self.table_widget_list_of_users.setIconSize(QSize(72, 72))
        self.table_widget_list_of_users.setSelectionBehavior(QTableView.SelectRows)


        self.set_menubar_about(self.showCredits)
        self.set_push_button_logout(self.closeApp)
        self.set_push_button_call(self.call_someone)

        """
        self.setWindowFlags(Qt.CustomizeWindowHint)


        self.setWindowFlags(
                QtCore.Qt.Window |
                QtCore.Qt.CustomizeWindowHint |
                QtCore.Qt.WindowTitleHint |
                QtCore.Qt.WindowCloseButtonHint |
                QtCore.Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        """
        # connect(self.close_event_message_box)
    def showCredits(self):
        self.creditsSignal.emit(True)

    def closeApp(self, event):
        print(event)
        self.close()

    def closeEvent(self, event):
        self.closingSignal.emit(event)

    def setUserName(self, user_name):
        self.userName = user_name

    def setUserAvatar(self, user_avatar):
        try:
            self.label_avatar.setPixmap(
                QtGui.QPixmap(self.prefix + str(user_avatar))
            )
        except Exception as err:
            print(err)

    def getList(self):
        payload = {"type": "d", "description": "GET"}
        data = json.dumps(payload).encode("utf-8")
        print("{*} MainWindow info : Sended data to server:", data)
        self.client.sendMessage(data)
        self.read()

    def call_someone(self):
        row = int(self.table_widget_list_of_users.currentRow())

        if row != None:
            try:
                where = self.table_widget_list_of_users.item(row, 0).text()
            except Exception as err:
                print(err)

            if where != None:
                print("Wybrano dzwonienie do ", where)
                payload = {"type": "d", "description": "INVITE", "call_to": where}
                data = json.dumps(payload).encode("utf-8")
                print(data)
                self.client.sendMessage(data)
                self.timer.start(5000)
                self.read()

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

    def showConnectionStatus(self, status):
        # self.addWidget(self.statusBar)
        self.statusBar.showMessage(status)

    def read(self):
        if self.waiting_for_signal():
            print("{*} MainWindow getting from Server:", self.client.received)
            if self.client.status == "202 USERS":
                print("{*} MainWindow users: ", self.client.users)
                self.set_who_is_signed(self.client.who_signed)
                print("{*} MainWindow info: Users - ",self.client.users)
                self.add_row_to_list_of_users(self.client.users)

            elif self.client.status == "200 INVITE":
                status = "Nawiązywanie polaczenia"
                self.showConnectionStatus(status)
                print(status)
            elif self.client.status == "406 INVITE":
                status = "Nie można się połączyć z wybranym użytkownikiem"
                self.showConnectionStatus(status)
                print(status)
            elif self.client.status == "200 END":
                status = "Zakonczono polaczenie"
                self.showConnectionStatus(status)
                self.client.send_ack_on_close_conn()
                print(status)
            elif self.client.status == "402 NOT ACCEPTABLE":
                status = "Aktywuj swoje konto"
                self.showConnectionStatus(status)
                print(status)

        else:
            status = "Serwer nie odpowiada"
            self.showConnectionStatus(status)
            print(status)
            print("{!} MainWindow error: Didn't get response")

    def keyPressEvent(self, event):
        """
            Close application from escape key.
        """
        if event.key() == Qt.Key_Escape:
            self.close()
