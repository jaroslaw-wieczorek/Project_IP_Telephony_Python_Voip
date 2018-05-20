from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from JaroEliCall.gui.adduser_ui import Ui_Form
from PyQt5.QtCore import pyqtSlot
from threading import Thread
import json

"""     List of contacts Widget
    Screen to load contacts and call to people
    __init__ - get list of people to table
    logout - logout   
    menu_rooms - going to list of available rooms
    call - call to person/people
"""

class AddUserWidget(QDialog, Ui_Form):
    def __init__(self, client):
        super(AddUserWidget, self).__init__()
        self.setupUi(self)
        self.c = client
        self.pushButton_3.clicked.connect(self.logout)
        self.pushButton_5.clicked.connect(self.menu_rooms)
        self.pushButton_4.clicked.connect(self.call)


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

        row = 0
        for a in diction:
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(a))
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(diction[a]))
            row = row + 1

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
        self.c.sendingVoice()




