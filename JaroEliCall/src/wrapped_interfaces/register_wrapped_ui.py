#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:49:10 2018

@author: afar
"""
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..','..'))
sys.path.append(lib_path)



from gui.register_ui import Ui_RegisterInterfaceDialog

from gui.resources import icons_wrapper_rc


class RegisterWrappedUI(QDialog, Ui_RegisterInterfaceDialog):
    def __init__(self):
        super(RegisterWrappedUI, self).__init__()
        self.setupUi(self)
        self.show()
        
    def set_login(self, login):
        self.line_edit_login.setText(login)
      
    def set_email(self, email):
        self.line_edit_email.setText(email)
        
    def set_password(self, password):
        """ Metoda dodatkowa """
        self.line_edit_password.setText(password)
    
    def set_repeat_password(self, repeat_assword):
        """ Metoda dodatkowa """
        self.line_edit_repeat_password.setText(repeat_assword)
        
    def validate_email(self):
        """ Metoda typu validate służy do sprawdzenia poprawności emaila """
        email = self.get_email()
        print(email)
        # Potrzebna walidacja maila
        
        
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
    
    def set_push_button_login(self, funct):
        self.psuh_button_login.clicked.connect(funct)
    
    def set_push_button_register(self, funct):
        self.push_button_register.clicked.connect(funct)
    
    def get_email(self):
        return self.line_edit_email.text()
    
    def get_password(self):
        return self.line_edit_password.text()

    def get_repeat_password(self):
        return self.line_edit_repeat_password.text()
     
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
    