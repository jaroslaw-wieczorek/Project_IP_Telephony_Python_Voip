#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:43:22 2018

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


from gui.interaction_ui import Ui_InteractionInterfaceDialog
from gui.resources import icons_wrapper_rc
from gui.resources import resources_avatars_rc


class InteractionWrappedUI(QDialog, Ui_InteractionInterfaceDialog):

    def __init__(self):
        super(InteractionWrappedUI, self).__init__()

        self.setupUi(self)

    def get_pixmap_from_resources(self, name):
        pixmap = QPixmap(str(":/icon/" + name))
        return pixmap

    def get_icon_from_resources(self, name):
        icon = QIcon(QPixmap(str(":/icon/" + name)))
        return icon

    def get_img_from_resources(self, name):
        pic = QImage(str(":/icon/" + name))
        return pic

    def set_user_call_text(self, who):
        self.rich_text_user_call.setText(str(who))

    def set_call_text(self, who):
        self.rich_text_user_call.setText(str(who))

    def set_push_button_accept(self, funct):
        self.push_button_accept.clicked.connect(funct)

    def set_push_button_reject(self, funct):
        self.push_button_reject.clicked.connect(funct)

    def set_label_accept_pixmap(self, name="call-in-progress.png"):
        self.label_accept.setPixmap(self.get_pixmap_from_resources(name))

    def set_label_reject_pixmap(self, name="call-ended.png"):
        self.label_reject.setPixmap(self.get_pixmap_from_resources(name))

    def set_avatar(self, pixmap):
        self.label_avatar.setPixmap(QPixmap(str(pixmap)))

    def nothing(self):
        print("Do nothing!")


"""

if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = InteractionWrappedUI()

    window.set_label_accept_pixmap()
    window.set_label_reject_pixmap()
        #self.set_label_reject_pixmap()
        #self.label_accept.text("gg")

    #window.test_add()
    window.show()
    sys.exit(app.exec_())

"""
