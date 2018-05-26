# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/interaction.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InteractionForm(object):
    def setupUi(self, InteractionForm):
        InteractionForm.setObjectName("InteractionForm")
        InteractionForm.resize(314, 348)
        self.verticalLayout = QtWidgets.QVBoxLayout(InteractionForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_user = QtWidgets.QLabel(InteractionForm)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_user.setFont(font)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setObjectName("label_user")
        self.verticalLayout.addWidget(self.label_user)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem)
        self.pic_1 = QtWidgets.QLabel(InteractionForm)
        self.pic_1.setMinimumSize(QtCore.QSize(100, 100))
        self.pic_1.setText("")
        self.pic_1.setPixmap(QtGui.QPixmap(":/ikony/icons/111317-essential-ui/svg/call-ended.svg"))
        self.pic_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_1.setObjectName("pic_1")
        self.horizontal_layout_1.addWidget(self.pic_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem1)
        self.pic_2 = QtWidgets.QLabel(InteractionForm)
        self.pic_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pic_2.setText("")
        self.pic_2.setPixmap(QtGui.QPixmap(":/ikony/icons/111317-essential-ui/svg/phone-call.svg"))
        self.pic_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_2.setObjectName("pic_2")
        self.horizontal_layout_1.addWidget(self.pic_2)
        spacerItem2 = QtWidgets.QSpacerItem(38, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontal_layout_1)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setSpacing(2)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem3)
        self.push_button_1 = QtWidgets.QPushButton(InteractionForm)
        self.push_button_1.setMinimumSize(QtCore.QSize(100, 70))
        self.push_button_1.setObjectName("push_button_1")
        self.horizontal_layout_2.addWidget(self.push_button_1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem4)
        self.push_button_2 = QtWidgets.QPushButton(InteractionForm)
        self.push_button_2.setMinimumSize(QtCore.QSize(100, 70))
        self.push_button_2.setObjectName("push_button_2")
        self.horizontal_layout_2.addWidget(self.push_button_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontal_layout_2)

        self.retranslateUi(InteractionForm)
        QtCore.QMetaObject.connectSlotsByName(InteractionForm)

    def retranslateUi(self, InteractionForm):
        _translate = QtCore.QCoreApplication.translate
        InteractionForm.setWindowTitle(_translate("InteractionForm", "Form"))
        self.label_user.setText(_translate("InteractionForm", "Tomek dzwoni"))
        self.push_button_1.setText(_translate("InteractionForm", "Odrzuć"))
        self.push_button_2.setText(_translate("InteractionForm", "Odbierz"))

from . import zasoby_rc
