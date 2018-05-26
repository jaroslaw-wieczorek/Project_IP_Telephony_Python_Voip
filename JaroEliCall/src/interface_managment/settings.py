from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', 'gui'))
sys.path.append(lib_path)


from .gui.settings_ui import Ui_SettingsDialog

class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setupUi(self)
        
