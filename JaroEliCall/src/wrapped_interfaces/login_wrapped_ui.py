#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 18:49:11 2018

@author: afar
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)


from gui.login_ui import Ui_LoginInterfaceDialog
#from gui.testpic_ui import Ui_Dialog
from gui.resources import icons_wrapper_rc


class LoginWrappedUI(QDialog, Ui_LoginInterfaceDialog):
    def __init__(self):
        super(LoginWrappedUI, self).__init__()
        self.setupUi(self)
                
    def set_info_text(self, text):
        self.label_info.setText(text)
    
    def clear_info_text(self):
        self.label_info.clear()
       
    def hide_info_text(self):
        self.label_info.hide()
        
    def show_info_text(self):
        self.label_info.show()
        
        
    def set_login(self, login):
        self.line_edit_login.setText(login)
      
        
    def set_password(self, password):
        """ Metoda dodatkowa """
        self.line_edit_password.setText(password)
        
        
    def get_login(self):
        """ Metoda typu get służy do pobrania wpisanego loginu"""
        if self.line_edit_login.text() != '' and self.line_edit_login.text() !=None:
            return self.line_edit_login.text()
        else:
            return None
        
    def get_password(self):
        return self.line_edit_password.text()

    
    def set_push_button_login(self, funct):
        self.push_button_login.clicked.connect(funct)
    
    def set_push_button_register(self, funct):
        self.push_button_register.clicked.connect(funct)

    def nothing(self):
        print("Do nothing!")
        
        