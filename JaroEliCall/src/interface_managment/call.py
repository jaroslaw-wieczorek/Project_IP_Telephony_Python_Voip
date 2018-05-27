#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:43:02 2018

@author: afar
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..','..', 'gui'))
sys.path.append(lib_path)


from call_ui import Ui_CallDialog


class CallDialog(QDialog, Ui_CallDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setupUi(self)
        
