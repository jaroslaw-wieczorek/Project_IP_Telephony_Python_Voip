from PyQt5 import QtCore, QtGui, QtWidgets

class SettingsDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(DialogWidget, self).__init__()
        self.setupUi(self)
