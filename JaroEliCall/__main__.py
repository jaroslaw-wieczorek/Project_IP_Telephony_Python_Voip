import sys
from JaroEliCall.src.actionsViews.LoginWidget_code import LoginWidget
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from JaroEliCall.gui.main_ui import Ui_MainWindow
from JaroEliCall.gui.settings_ui import Ui_SettingsDialog

class Dialog(QDialog, Ui_SettingsDialog):
    def __init__(self, no):
        super(Dialog, self).__init__()
        self.setupUi(self)
    
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
      
        self.actSettings.triggered.connect(self.showSettings)
        
    def showSettings(self):
        self.s = Dialog(QDialog())
        self.s.setupUi(self.s)
        self.s.show()

        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    # main_window.show()

    users = LoginWidget()
    users.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

