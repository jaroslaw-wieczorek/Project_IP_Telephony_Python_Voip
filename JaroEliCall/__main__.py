import sys
from JaroEliCall.src.actionsViews.LoginWidget_code import LoginWidget
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

    window = LoginWidget()
    window.show()

    sys.exit(app.exec_())

    print("koNIEC LOGIN Widget")


if __name__ == "__main__":
    main()

