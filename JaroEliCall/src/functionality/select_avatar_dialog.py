import os
import sys
from lxml import etree

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

mypath = os.path.abspath(os.path.join(__file__, '..', '..',
                                      '..', 'gui', 'resources'))
sys.path.append(mypath)
print(mypath)

import resources_avatars_rc


class SelectAvatar(QDialog):
    def __init__(self, parent=None, avatar=None):
        super(SelectAvatar, self).__init__(avatar)
        self.avatar = avatar
        self.parent = parent
        self.avatar_names = []
        self.setMinimumHeight(500)
        self.setMinimumWidth(550)
        self.setWindowTitle("Wybór avatara")

        self.setNames()

        print(self.avatar_names)

        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setIconSize(QSize(72, 72))
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSelectionMode(QListView.SingleSelection)

        self.addAvatarsToList()

        self.push_ok = QPushButton("Wybierz")
        self.push_ok.clicked.connect(self.return_selected_avatar)

        self.vert = QVBoxLayout()
        self.vert.setContentsMargins(10,20,10,20)
        self.vert.addWidget(self.listWidget)
        self.vert.addWidget(self.push_ok)
        self.setLayout(self.vert)
        #self.show()

    def setNames(self):
         for i, elem in etree.iterparse(mypath + '/resources_avatars.qrc', tag='file'):
            self.avatar_names.append(elem.text.split("/")[-1])

    def addAvatarsToList(self):
        self.listWidget.clear()

        for name in self.avatar_names:
            item = QListWidgetItem()
            icon = QIcon()
            icon.addPixmap(QPixmap(":/avatars/" + str(name)),
                           QIcon.Normal, QIcon.Off)

            item.setIcon(icon)
            item.setSizeHint(QSize(100, 100))
            item.setTextAlignment(Qt.AlignCenter);
            item.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(name)

            self.listWidget.addItem(item)


    def return_selected_avatar(self):
        self.avatar = self.listWidget.currentItem()
        if self.avatar is None or self.avatar == []:
            print("{*} SelectAvatar dialog info: avatar is None or [] !!!")
            self.parent.label_avatar_name.setText("None")
            #return None
            #self.parent.label_avatar_name.setText(self.avatar.text())
            #pixmap = self.avatar.icon().pixmap(QSize(100, 100))
            #self.parent.label_avatar.setPixmap(pixmap)
        else:
            print(self.avatar.text())
            self.parent.label_avatar_name.setText(self.avatar.text())
            pixmap = self.avatar.icon().pixmap(QSize(100, 100))
            self.parent.label_avatar.setPixmap(pixmap)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SelectAvatar()


    sys.exit(app.exec_())
