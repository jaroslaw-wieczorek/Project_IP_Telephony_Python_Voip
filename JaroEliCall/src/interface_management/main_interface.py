#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:47:29 2018

@author: afar
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'gui'))
sys.path.append(lib_path)


from main_interface_ui import Ui_MainWindowInterface

class MainWindow(QMainWindow, Ui_MainWindowInterface):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        

