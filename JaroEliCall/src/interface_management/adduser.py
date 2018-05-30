#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:42:22 2018

@author: afar
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)
print(lib_path)


from gui.adduser_ui import Ui_FormInterface
#from gui.testpic_ui import Ui_Dialog
from gui.resources import icons_wrapper_rc


class AdduserDialog(QDialog, Ui_FormInterface):
    
    def __init__(self):
        super(AdduserDialog, self).__init__()
       
        self.setupUi(self)
        
        
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
        self.push_button_logout.clicked.connect(funct
                                                
                                                )
    def set_push_button_call(self, funct):
        self.push_button_call.clicked.connect(funct)    
        
        
    def set_push_button_invite(self, funct):
        self.push_button_invite.clicked.connect(funct)
        
        
    def set_avatar(self, pixmap : QPixmap):
        self.label_avatar.setPixmap(QPixmap(str(pixmap)))
    
    
    def set_fit_width(self):
        self.table_widget_list_of_users.horizontalHeader().setStretchLastSection(True);
        
        
    def set_value_on_list_of_users(self, row, col, item: QTableWidgetItem):
        self.table_widget_list_of_users.setItem(row, col, item)
        
        
    def add_row_to_list_of_users(self, item):
        newRowNum = self.table_widget_list_of_users.rowCount()
        self.table_widget_list_of_users.insertRow(newRowNum)
        for cell, value in enumerate(item):
            self.table_widget_list_of_users.setItem(newRowNum, cell, QTableWidgetItem(str(value)))
    
           
    def nothing(self):
        print("Do nothing!")
        
        

#Fot tests
"""
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = AdduserDialog()
    window.set_push_button_logout(window.nothing)
    window.set_push_button_call(window.nothing)
    window.set_push_button_invite(window.nothing)
    window.set_fit_width()
    window.add_row_to_list_of_users(["jaro", 77,"avatar"])
  
    item = QTableWidgetItem()
    item.setIcon(window.get_icon_from_resources("strategy.png"))
    
    window.set_value_on_list_of_users(1,0,item)    
    #window.test_add()
    window.show()
    sys.exit(app.exec_())
"""