from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import QSize


import os
import sys

lib_path = os.path.abspath(os.path.join(__file__, '..', '..', 'resources'))
sys.path.append(lib_path)
print(lib_path)

import resources_avatars_rc
from lxml import etree


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    listWidget = QListWidget()
    listWidget.setViewMode(QtWidgets.QListView.IconMode)

    images_names = []
    for _, elem in etree.iterparse(lib_path + '/resources_avatars.qrc', tag='file'):
        images_names.append(elem.text.split("/")[-1])

    for x in images_names:
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/avatars/" + str(x)),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)

        item.setIcon(icon)
        listWidget.addItem(item)
        listWidget.setIconSize(QSize(72, 72))

    vert = QVBoxLayout()
    vert.addWidget(listWidget)

    mainwindow.setCentralWidget(listWidget)
    mainwindow.show()

    sys.exit(app.exec_())
