#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:42:22 2018

@author: afar
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTableWidget

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)

from gui.resources import zasoby_rc

from gui.adduser_ui import Ui_FormInterface

class AdduserDialog(QDialog, Ui_FormInterface):
    def __init__(self):
        super(AdduserDialog, self).__init__()
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/111317-essential-ui/png/profile-user-1.png"), QIcon.Active, QIcon.Off)
        self.setupUi(self)
        
    def set_push_button_logout(self, funct):
        self.push_button_logout.clicked.connect(funct)
    def set_push_button_call(self, funct):
        self.push_button_call.clicked.connect(funct)       
    def set_push_button_invite(self, funct):
        self.push_button_invite.clicked.connect(funct)
        
    def set_avatar(self, pic):
        self.label_avatar.setPixmap(QPixmap(str(pic)))
    
    def set_fit_width(self):
        self.tab_widget_list_of_users.horizontalHeader().setStretchLastSection(True);
        
    def nothing(self):
        print("Do nothing!")
        
        
"""
#Fot tests

if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = AdduserDialog()
    window.set_push_button_logout(window.nothing)
    window.set_push_button_call(window.nothing)
    window.set_push_button_invite(window.nothing)
    window.set_fit_width()
    window.show()
    sys.exit(app.exec_())
"""