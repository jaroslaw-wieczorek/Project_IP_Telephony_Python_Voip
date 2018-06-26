
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox

from JaroEliCall.gui.adduser_ui import Ui_FormInterface
from PyQt5.QtCore import pyqtSlot
from threading import Thread
import threading

import os
import sys

import json

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

from interface_management.adduser import AdduserDialog
from JaroEliCall.src.client import Client

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem


from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTableWidget

"""     List of contacts Widget
    Screen to load contacts and call to people
    __init__ - get list of people to table
    logout - logout   
    menu_rooms - going to list of available rooms
    call - call to person/people
"""

class AddUserWidget(AdduserDialog):

    def __init__(self, client):
        super(AddUserWidget, self).__init__()
        self.c = client
        self.closeEvent = self.notify

        self.getList()

        #podpięcie metod z AddUserWidget do przycisków interfejsu
        self.set_push_button_logout(self.logout)
        self.set_push_button_invite(self.menu_rooms)
        self.set_push_button_call(self.call)

        #poszerzenie kolumn tabeli do szerokości widżetu
        self.set_fit_width()

    def getList(self):
        payload = {"type": "d", "description": "GET"}
        data = json.dumps(payload).encode("utf-8")
        print("Wysłano do serwera:", data)
        self.c.sendMessage(data)


    def updateMongo(self, user_ip):
        print(user_ip)
        payload = {"type": "d", "description": "LOGOUT"}

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)


    @pyqtSlot()
    def logout(self):
        print("Wylogowanie")
        self.updateMongo(self.c.host)

    @pyqtSlot()
    def menu_rooms(self):
        print("Jestem u siebie")

    @pyqtSlot()
    def call(self):
        where = self.table_widget_list_of_users.currentItem().text()
        print("Wybrano dzwonienie do ", where)

    def notify(self, event):
        if self.close_event_message_box(event) == QMessageBox.Yes:
            self.logout()
            event.accept()
        else:
            event.ignore()
        
        #self.logout()
        print("notified")

"""
# For tests   
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = AddUserWidget(" ")
  
    window.show()
    sys.exit(app.exec_())
"""