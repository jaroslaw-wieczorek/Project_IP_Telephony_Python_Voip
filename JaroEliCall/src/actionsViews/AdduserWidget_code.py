from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from JaroEliCall.gui.adduser_ui import Ui_Form
from PyQt5.QtCore import pyqtSlot
from threading import Thread
import threading
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
        answer = self.c.sendMessage(("d GET").encode("utf-8"))[3:]
        diction = {}
        result = answer.replace("[[","[")
        result = result.replace("]]","]")

        jdata = json.loads(result)
        for d in jdata:
            diction[d['login']]=d['status']

        row = 0
        for a in diction:
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(a))
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(diction[a]))
            row = row + 1

        self.thread = Thread(target=self.c.listening, args=[])
        self.thread.start()

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




