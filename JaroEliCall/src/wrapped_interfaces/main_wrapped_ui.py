#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:42:22 2018

@author: afar
"""

import os
import sys

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem


lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)
print(lib_path)


from gui.main_ui import Ui_MainInterfaceDialog
from gui.resources import icons_wrapper_rc
from gui.resource import resources_avatars_rc


class MainWrappedUI(QDialog, Ui_MainInterfaceDialog):

    def __init__(self):
        super(MainWrappedUI, self).__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.label_avatar.setSize(QSize(90, 90))
        self.vertical_layout_left.addWidget(self.statusBar)

        self.set_fit_width()

    def set_info_text(self, text):
        self.label_info.setText(text)

    def clear_info_text(self):
        self.label_info.clear()

    def hide_info_text(self):
        self.label_info.hide()

    def show_info_text(self):
        self.label_info.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def get_pixmap_from_resources(self, name):
        pixmap = QPixmap(str(":/icon/" + name))
        return pixmap

    def get_icon_from_resources(self, name):
        icon = QIcon(QPixmap(str(":/icon/" + name)))
        return icon

    def get_img_from_resources(self, name):
        img = QImage(str(":/icon/" + name))
        return img

    def set_push_button_logout(self, funct):
        self.push_button_logout.clicked.connect(funct)

    def set_push_button_call(self, funct):
        self.push_button_call.clicked.connect(funct)

    def set_push_button_invite(self, funct):
        self.push_button_invite.clicked.connect(funct)

    def set_avatar(self, pixmap):
        self.label_avatar.setPixmap(QPixmap(str(pixmap)))

    def set_fit_width(self):
        self.table_widget_list_of_users.horizontalHeader().setStretchLastSection(True)

    def set_value_on_list_of_users(self, row, col, item):
        self.table_widget_list_of_users.setItem(row, col, item)

    def add_row_to_list_of_users(self, users):
        who_is_signed = self.label_user_name.text()
        for user in users:
            if user['login'] != who_is_signed:
                newRowNum = self.table_widget_list_of_users.rowCount()
                self.table_widget_list_of_users.insertRow(newRowNum)
                self.table_widget_list_of_users.setItem(newRowNum, 0, QTableWidgetItem(str(user['login'])))
                self.table_widget_list_of_users.setItem(newRowNum, 1, QTableWidgetItem(str(user['status'])))

                item = QTableWidgetItem()
                item.setIcon(QtGui.QPixmap(":/avatars/" + str(user['avatar'])), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.table_widget_list_of_users.setItem(newRowNum, 2, "")
                self.table_widget_list_of_users.setCellWidget(newRowNum, 2, item)


    def set_who_is_signed(self, who_is_signed):
        self.label_user_name.setText(who_is_signed)

    def delete_rows_users(self):
        self.table_widget_list_of_users.setRowCount(0)

    def close_event_message_box(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Wylogowywanie',
            "Czy napewno chcesz zakończyć? ", QMessageBox.Yes, QMessageBox.No)

        return reply


    def nothing(self):
        print("Do nothing!")


"""
#Fot tests

if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = MainWrappedUI()
    window.set_push_button_logout(window.nothing)
    window.set_push_button_call(window.nothing)
    window.set_push_button_invite(window.nothing)
    window.set_fit_width()
    #window.add_row_to_list_of_users(["jaro", "online","avatar"])

    item = QTableWidgetItem()
    item.setIcon(window.get_icon_from_resources("strategy.png"))

    window.set_value_on_list_of_users(1,0,item)
    #window.test_add()
    window.show()
    sys.exit(app.exec_())
"""
