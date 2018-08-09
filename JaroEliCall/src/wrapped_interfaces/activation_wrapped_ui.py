#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:49:10 2018

@author: afar
"""
import os
import sys


from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from PyQt5 import QtCore

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem



# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..','..'))
sys.path.append(lib_path)


from gui.resources import icons_wrapper_rc
from gui.password_change_ui import Ui_ActivationInterfaceDialog



class PasswordChangeWrappedUI(QDialog, Ui_ActivationInterfaceDialog):
    def __init__(self):
        super(PasswordChangeWrappedUI, self).__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()

        print("PasswordChangeWrappedUI", self.label_avatar.text())

    def validate_compare_passwords(self):
        """ Metoda typu validate służy do sprawdzenia tozsamości haseł """
        if self.get_password() == self.get_repeat_password():
            return True
        else:
            return False


    def get_login(self):
        """ Metoda typu get służy do pobrania wpisanego loginu"""
        if self.line_edit_login.text() != '' and self.line_edit_login.text() !=None:
            return self.line_edit_login.text()
        else:
            return None


    def set_push_button_already_account(self, funct):
        self.push_button_already_account.clicked.connect(funct)


    def set_change_password_button(self, funct):
        self.push_button_change_password.clicked.connect(funct)


    def get_email(self):
        return self.line_edit_email.text()


    def get_password_activate(self):
        return self.line_edit_password.text()


    def get_repeat_password_activate(self):
        return self.line_edit_repeat_password.text()

    def get_avatar_name(self):
        return self.label_avatar_name.text()

    def nothing(self):
        print("Do nothing!")



"""
For tests
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = RegisterForm()
    window.show()
    sys.exit(app.exec_())
"""
