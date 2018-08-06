#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 18:49:11 2018

@author: afar
"""
import os
import sys
import hashlib

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QStatusBar


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
        self.statusBar = QStatusBar()
        self.verticalLayout.addWidget(self.statusBar)
                
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
        self.line_edit_password.setText(password)
        
        
    def get_login(self):
        if self.line_edit_login.text() != '' and self.line_edit_login.text() != None:
            return str(self.line_edit_login.text())
        else:
            return None
        
    def get_password(self):
        print("haslo: ", self.line_edit_password.text())
        a = self.line_edit_password.text().replace(" ", "")
        print(a)
        print(len(a))
        print(hashlib.sha256(a.encode()).hexdigest())
        return hashlib.sha256(a.encode()).hexdigest()

    
    def set_push_button_login(self, funct):
        self.push_button_login.clicked.connect(funct)
    
    def set_push_button_register(self, funct):
        self.push_button_register.clicked.connect(funct)

    def nothing(self):
        print("Do nothing!")
        
        