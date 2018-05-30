import os
import sys


lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)


import json
from threading import Thread

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem


from interface_management.adduser import AdduserDialog





"""     List of contacts Widget
    Screen to load contacts and call to people
    __init__ - get list of people to table
    logout - logout   
    menu_rooms - going to list of available rooms
    call - call to person/people
"""

class MainWidget(AdduserDialog):
    def __init__(self, client):
        super(MainWidget, self).__init__()

        self.c = client
        self.set_push_button_logout(self.logout)
        self.set_push_button_invite(self.menu_rooms)
        self.set_push_button_call(self.call)
        self.set_fit_width()
        
        """self.pushButton_3.clicked.connect(self.logout)
        self.pushButton_5.clicked.connect(self.menu_rooms)
        self.pushButton_4.clicked.connect(self.call)"""


    def load_contracts(self):
        print("Wysylanie get")
        coll = self.c.sendMessage(("d GET").encode("utf-8"))
        coll = coll[3:]
        print("Odp: ", coll)

        diction = {}

        res = coll.replace("[[","[")
        res = res.replace("]]","]")
        print(res)
        jdata = json.loads(res)
        print(jdata)
        for d in jdata:
            print(d)
            print(d['login'])
            diction[d['login']]=d['status']

        print("zALADOWANO LISTE")

        print(diction)
        print(type(diction))
        print("Slownik")

        for row in diction:
            self.add_row_to_list_of_users(row)

        thread = Thread(target=self.c.listening, args=[])
        thread.start()

    @pyqtSlot()
    def logout(self):
        print("Wylogowanie")

    @pyqtSlot()
    def menu_rooms(self):
        pass

    @pyqtSlot()
    def call(self):
        s = "d INVITE Jarek".encode("utf-8")
        thread = Thread(target=self.c.sendMessage, args=(s,))
        thread.start()




# For tests   
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget(" ")
  
    window.show()
    sys.exit(app.exec_())

