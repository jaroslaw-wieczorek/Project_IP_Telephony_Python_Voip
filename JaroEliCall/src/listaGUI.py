from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
import loginGUI
import ast

uifile_2 = 'lista.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class listaGUI(base_2, form_2):
    def __init__(self, client):
        super(base_2, self).__init__()
        self.setupUi(self)
        self.c = client

        """       Ładowanie listy pracownikow z serwera            """
        self.data = ("GET ").encode("utf-8")
        print(self.data)
        try:
            self.c.sendMessage(self.data)
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
            self.tableWidget.setItem(0,0, QTableWidgetItem(diction["login"]))
            self.tableWidget.setItem(0,1, QTableWidgetItem(diction["status"]))


        self.menu_button.clicked.connect(self.on_menu_button_clicked)
        self.call_button.clicked.connect(self.on_call_button_clicked)
        self.logout_button.clicked.connect(self.on_logout_button_clicked)


    @pyqtSlot()
    def on_menu_button_clicked(self):
        self.main = loginGUI()
        self.main.show()
        self.close()

    @pyqtSlot()
    def on_call_button_clicked(self):
        pass
        # pobranie informacji o pozostałych klientach


    @pyqtSlot()
    def on_logout_button_clicked(self):
        pass

