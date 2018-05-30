import os
import sys
import json
import threading
from threading import Thread

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

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
        #podpięcie metod z AddUserWidget do przycisków interfejsu
        self.set_push_button_logout(self.logout)
        self.set_push_button_invite(self.menu_rooms)
        self.set_push_button_call(self.call)
        
        #poszerzenie kolumn tabeli do szerokości widżetu 
        self.set_fit_width()
        
    def load_contracts(self):
        answer = self.c.sendMessage(("d GET").encode("utf-8"))[3:]
        diction = {}
        result = answer.replace("[[","[")
        result = result.replace("]]","]")

        jdata = json.loads(result)
        for d in jdata:
            diction[d['login']]=d['status']

        #Uproszczona metoda dodawania użytkowników
        for row in diction:
            self.add_row_to_list_of_users(row)

        self.thread = Thread(target=self.c.listening, args=[])
        self.thread.start()
        
        #Po prostu print lololololo
        print("lololololo")


    def updateMongo(self, user_ip):
        print(user_ip)
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
        s = "d INVITE Jarek".encode("utf-8")
        thread = Thread(target=self.c.sendMessage, args=(s,))
        thread.start()

"""
# For tests   
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = AddUserWidget(" ")
  
    window.show()
    sys.exit(app.exec_())
"""