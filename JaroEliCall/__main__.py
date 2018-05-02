import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from JaroEliCall.gui.mainwindow_ui import Ui_MainWindow
from JaroEliCall.gui.loging_ui import Ui_Form

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

class DialogWidget(QDialog, Ui_Form):
   def __init__(self):
       super(DialogWidget, self).__init__()
       self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    dialog = DialogWidget()
    dialog.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


