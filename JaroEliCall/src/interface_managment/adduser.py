#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:42:22 2018

@author: afar
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'gui'))
sys.path.append(lib_path)


from adduser_ui import Ui_FormInterface

class AdduserDialog(QDialog, Ui_FormInterface):
    def __init__(self):
        super(AdduserDialog, self).__init__()
        self.setupUi(self)
        
