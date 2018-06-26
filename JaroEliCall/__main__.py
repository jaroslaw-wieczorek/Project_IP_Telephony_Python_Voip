import sys
from JaroEliCall.src.actionsViews.LoginWidget_code import LoginWidget
from JaroEliCall.src.actionsViews.LoginWidget_code import AddUserWidget

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from JaroEliCall.src.interface_management.settings import SettingsDialog
from JaroEliCall.src.actionsViews.MainWidget_code import MainWidget
from JaroEliCall.src.client import Client
from threading import Thread

       
def main():
    app = QApplication(sys.argv)
    # main_window.show()

    client = Client("192.168.0.102", 50001)
    window = LoginWidget(client)
    window.show()

    if(app.exec_() ==QDialog.Accepted):
        print("Gramy dalej: ")
    else:
        print("Zakmnelam LoginWidget")
        lol = AddUserWidget(client)
        print("Pokazuje")
        lol.show()
        print("Ece bo chce")


    sys.exit(app.exec_())



if __name__ == "__main__":
    main()

