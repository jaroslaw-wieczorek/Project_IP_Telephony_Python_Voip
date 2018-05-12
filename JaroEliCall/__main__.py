import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from JaroEliCall.gui.mainwindow_ui import Ui_MainWindow
from JaroEliCall.src.actionsViews.LoginWidget_code import LoginWidget
from JaroEliCall.src.actionsViews.AdduserWidget_code import AddUserWidget
from JaroEliCall.src.tmp.client import Client

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    users = LoginWidget()
    users.show()
    """users = AddUserWidget(client)
    users.show()"""

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


