
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

lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)


from interface_management.adduser import AdduserDialog

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
        #podpięcie metod z AddUserWidget do przycisków interfejsu
        self.set_push_button_logout(self.logout)
        self.set_push_button_invite(self.menu_rooms)
        self.set_push_button_call(self.call)
        
        #poszerzenie kolumn tabeli do szerokości widżetu 
        self.set_fit_width()
        
    def load_contracts(self):
        print("LOAD")
        payload = {"type": "d", "description": "GET"}

    def add_row_to_list_of_users(self, packet):
        print("Lista kontaktow: ", packet)


    def updateMongo(self, user_ip):
        print(user_ip)
        print("MONGO UPDATE CLIENT c.sendMessage THREAD")
        s = ("d LOGOUT").encode("utf-8")
        thread = Thread(target=self.c.sendMessage, args=(s,))
        thread.start()
        self.close()

    @pyqtSlot()
    def logout(self):
        print("Wylogowanie")
        self.updateMongo(self.c.host)

    @pyqtSlot()
    def menu_rooms(self):
        pass

    @pyqtSlot()
    def call(self):
        print("CALL CLIENT c.sendMessage THREAD")
        s = "d INVITE Jarek".encode("utf-8")
        thread = Thread(target=self.c.sendMessage, args=(s,))
        thread.start()
        
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