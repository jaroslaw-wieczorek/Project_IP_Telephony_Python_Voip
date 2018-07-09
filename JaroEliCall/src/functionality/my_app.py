import os
import sys

from PyQt5.QtWidgets import QApplication


src_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(src_path)

# from JaroEliCall.src.functionality.login_dialog import LoginDialog
# from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
# from JaroEliCall.src.functionality.register_dialog import RegisterDialog
# from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog


class MyApp(QApplication):

    def __init__(self, argv):
        super(MyApp).__init__()
   
        self.mainWindow = None
        self.loginWindow = None
        self.registerWindow = None

    # MainWindow Dialog methods
    def setupMainWindow(self, main_window):
        self.mainWindow = main_window


    def hideMainWindow(self):
        self.mainWindow.hide()


    def showMainWindow(self):
        self.mainWindow.show()
     
    # Login Dialog methods
    def setupLoginWindow(self, login_window):
        self.loginWindow = login_window


    def hideLoginWindow(self):
        self.loginWindow.hide()


    def showLoginWindow(self):
        self.loginWindow.show()

    # Register Dialog methods
    def setupRegisterWindow(self, register_window):
        self.registerWindow = register_window


    def hideRegisterWindow(self):
        self.registerWindow.hide()


    def showRegisterWindow(self):
        self.registerWindow.show()
