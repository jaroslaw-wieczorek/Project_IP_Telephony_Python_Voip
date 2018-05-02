import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from JaroEliCall.gui.mainwindow_ui import Ui_MainWindow
from JaroEliCall.src.actionsViews.LoginWidget_code import LoginWidget
from JaroEliCall.src.actionsViews.RegisterWidget_code import RegisterWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    login = LoginWidget()
    login.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


