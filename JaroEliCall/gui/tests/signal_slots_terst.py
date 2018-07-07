import sys
from os import getcwd

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSlot

class From(QtWidgets.QDialog):    
    def __init__(self, parent=None):
        super(From, self).__init__(parent)

        self.ui=uic.loadUi("basic.ui",self)
        self.ui.pushButton.clicked.connect(self.add_number)   
      

        self.ui.labelImagen   = QtWidgets.QLabel()   
        self.ui.show()

    @pyqtSlot()
    def add_number(self):
        fileName, dummy = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open image file...", getcwd(),
            "Image (*.png *.jpg)",
            options=QtWidgets.QFileDialog.Options())
        if fileName:
            pix = QtGui.QPixmap(fileName)
            self.ui.labelImagen.setPixmap(pix)  
            self.ui.labelImagen.show()            


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    w=From()
    sys.exit(app.exec())