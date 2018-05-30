#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:49:10 2018

@author: afar
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..','..', 'gui'))
sys.path.append(lib_path)



from register_ui import Ui_RegisterForm


class RegisterForm(QWidget, Ui_RegisterForm):
    def __init__(self):
        super(RegisterForm, self).__init__()
        self.setupUi(self)
        self.show()

        
""" 
For tests
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = RegisterForm()
    window.show()
    sys.exit(app.exec_())
"""
    