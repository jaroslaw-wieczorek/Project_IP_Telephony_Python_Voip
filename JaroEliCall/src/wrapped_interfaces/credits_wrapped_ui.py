#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:43:10 2018

@author: afar
"""

import os
import sys

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem


lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)

from gui.credits_ui import Ui_CreditsInterfaceDialog
from gui.resources import icons_wrapper_rc
from gui.resources import avatars


class CreditsWrappedUI(QDialog, Ui_CreditsInterfaceDialog):

    def __init__(self):
        super(CreditsWrappedUI, self).__init__()

        self.setupUi(self)
