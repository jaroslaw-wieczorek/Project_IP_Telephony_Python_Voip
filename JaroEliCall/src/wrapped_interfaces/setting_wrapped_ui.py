from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..','..', 'gui'))
sys.path.append(lib_path)


from settings_ui import Ui_SettingsInterfaceDialog

from gui.resources import icons_wrapper_rc

class SettingsWrappedUI(QDialog, Ui_SettingsInterfaceDialog):
    def __init__(self):
        super(SettingsWrappedUI, self).__init__()
        self.setupUi(self)
        
        # TODO
"""  
Fot tests

if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = SettingsDialog()
    window.show()
    sys.exit(app.exec_())
"""