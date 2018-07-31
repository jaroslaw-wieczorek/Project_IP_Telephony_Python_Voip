import os
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.a = Avatar()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.pixmap = QPixmap(self.a.getIcon())
        lbl.setPixmap(self.pixmap)
        self.lbl = QLabel()
        #self.lbl.setText("Text")

        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


class Avatar:
    def __init__(self):
        self.icon = (
            '0000010001001010000001002000680400001600000028000000100000002000000001'
            '0020000000000000040000130b0000130b00000000000000000000000000000773e600'
            '0577df000877dd060477df490277e0a70277e0e30277e0fb0277e0fb0277e0e30277e0'
            'a70377e0490577e0060377e1000175f00000000000000000000377e0000577df180377'
            'e0920277e0ed0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0277e0ed02'
            '77e0920377e1180277e100000000000577df000577df180277e0b10177e0ff0177e0ff'
            '0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0277e0'
            'b10377e1180377e1000174de070176df920076e0ff0077e0ff0177e0ff0177e0ff0177'
            'e0ff0076e0ff0076e0ff0177e0ff0177e0ff0177e0ff0077e0ff0076e0ff0176e09202'
            '76e107127fe0481983e2ee1f87e3ff0d7de1ff0076e0ff0077e0ff067ae1ff1d86e3ff'
            '1a84e3ff077ae1ff0177e0ff0076e0ff0e7ee1ff1e87e3ff1581e2ee0a7be1483592e4'
            'a759a6e9ff4fa0e8ff66adeaff1e86e3ff0b7ce1ff60a9e9ff57a5e9ff56a4e9ff459b'
            'e7ff0277e0ff288ce4ff68aeeaff51a1e8ff56a4e8ff2389e3a70578e0e40177e0ff00'
            '72dfff499de7ff4fa1e8ff3c96e6ff53a3e8ff0074dfff0075e0ff0579e0ff0478e0ff'
            '6cb0ebff268be4ff0075e0ff0378e0ff0478e0e40176e0fb1481e2ff439ae7ff7bb8ec'
            'ff2a8ce4ff5da8eaff63abeaff3793e5ff3894e6ff3392e5ff1481e2ff73b4edff0b7c'
            'e1ff0177e0ff0177e0ff0277e0fb2c8de4fb76b5ecff50a1e8ff1e86e3ff0075e0ff59'
            'a6e9ff63abeaff3692e5ff3793e5ff76b5ecff2389e3ff73b4ecff0d7de1ff0077e0ff'
            '0077e0ff0177e0fb5ea8e9e455a4e8ff0075e0ff0b7ce1ff0679e0ff3090e5ff59a6e9'
            'ff0377e0ff1380e2ff62abe9ff0c7ce1ff65aceaff3693e5ff0478e0ff0d7de1ff077a'
            'e1e42489e2a75ba7e9ff59a5e9ff5aa6e9ff1983e2ff0578e0ff489de7ff5da8eaff5f'
            'a9eaff2c8ee4ff0075e0ff1a84e2ff60aaeaff5ba6e9ff57a4e9ff1f86e3a70075df48'
            '0478e0ee0e7ee1ff087be1ff0177e0ff0177e0ff0177e0ff0c7de1ff087be1ff0076e0'
            'ff0177e0ff0076e0ff0479e0ff0e7ee1ff087ae1ee0377e0480777de070377e0920177'
            'e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff01'
            '77e0ff0177e0ff0177e0ff0277e0920477e1070577df000577df180277e0b10177e0ff'
            '0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0'
            'ff0277e0b10377e1180377e100000000000377e0000577df180377e0920277e0ed0177'
            'e0ff0177e0ff0177e0ff0177e0ff0177e0ff0177e0ff0277e0ed0277e0920377e11802'
            '77e10000000000000000000773e6000577df000877dd060477df490277e0a70277e0e3'
            '0277e0fb0277e0fb0277e0e30277e0a70377e0490676e0060377e1000174f300000000'
            '00e0070000c00300008001000000000000000000000000000000000000000000000000'
            '00000000000000000000000000000000000080010000c0030000e0070000')

    def getIcon(self):
        image = QtGui.QImage()
        image.loadFromData(QtCore.QByteArray.fromHex(self.icon))
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image)
        return QtGui.QIcon(pixmap)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


if __name__ == "__main__":
    main()
