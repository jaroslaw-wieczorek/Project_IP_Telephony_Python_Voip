from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from JaroEliCall.gui.adduser_ui import Ui_Form
from PyQt5.QtCore import pyqtSlot
import ast

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
        self.load_Contracts()
        self.pushButton_2.clicked.connect(self.logout)
        self.pushButton_3.clicked.connect(self.menu_rooms)
        self.pushButton.clicked.connect(self.call)

    def load_Contracts(self):
        try:
            self.c.sendMessage(("GET ").encode("utf-8"))
            print("Wysłano")
        except ConnectionRefusedError as err:
            print(err)

        coll = self.c.wait4Response()[3:]
        print(coll)

        diction = ast.literal_eval(coll)
        print(diction["login"])
        print(diction["status"])

        print(diction)

        for a in diction:
            self.tableWidget.setItem(0, 0, QTableWidgetItem(diction["login"]))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(diction["status"]))


    @pyqtSlot()
    def logout(self):
        pass

    @pyqtSlot()
    def menu_rooms(self):
        pass

    @pyqtSlot()
    def call(self):
        pass




