# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/loging.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(396, 483)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(LoginFSSorm)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.vertical_layout_main = QtWidgets.QVBoxLayout()
        self.vertical_layout_main.setObjectName("vertical_layout_main")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_main.addItem(spacerItem1)
        self.horizontal_layout_login = QtWidgets.QHBoxLayout()
        self.horizontal_layout_login.setObjectName("horizontal_layout_login")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_login.addItem(spacerItem2)
        self.label_login = QtWidgets.QLabel(LoginForm)
        self.label_login.setObjectName("label_login")
        self.horizontal_layout_login.addWidget(self.label_login)
        self.line_edit_login = QtWidgets.QLineEdit(LoginForm)
        self.line_edit_login.setObjectName("line_edit_login")
        self.horizontal_layout_login.addWidget(self.line_edit_login)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_login.addItem(spacerItem3)
        self.vertical_layout_main.addLayout(self.horizontal_layout_login)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_main.addItem(spacerItem4)
        self.horizontal_layout_password = QtWidgets.QHBoxLayout()
        self.horizontal_layout_password.setObjectName("horizontal_layout_password")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_password.addItem(spacerItem5)
        self.label_pass = QtWidgets.QLabel(LoginForm)
        self.label_pass.setObjectName("label_pass")
        self.horizontal_layout_password.addWidget(self.label_pass)
        self.line_edit_pass = QtWidgets.QLineEdit(LoginForm)
        self.line_edit_pass.setMinimumSize(QtCore.QSize(0, 0))
        self.line_edit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_pass.setObjectName("line_edit_pass")
        self.horizontal_layout_password.addWidget(self.line_edit_pass)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_password.addItem(spacerItem6)
        self.vertical_layout_main.addLayout(self.horizontal_layout_password)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_main.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.vertical_layout_main)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontal_layout_buttons = QtWidgets.QHBoxLayout()
        self.horizontal_layout_buttons.setSpacing(2)
        self.horizontal_layout_buttons.setObjectName("horizontal_layout_buttons")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons.addItem(spacerItem9)
        self.push_button_register = QtWidgets.QPushButton(LoginForm)
        self.push_button_register.setObjectName("push_button_register")
        self.horizontal_layout_buttons.addWidget(self.push_button_register)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons.addItem(spacerItem10)
        self.push_button_login = QtWidgets.QPushButton(LoginForm)
        self.push_button_login.setObjectName("push_button_login")
        self.horizontal_layout_buttons.addWidget(self.push_button_login)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttons.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontal_layout_buttons)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
        LoginForm.setTabOrder(self.line_edit_login, self.line_edit_pass)
        LoginForm.setTabOrder(self.line_edit_pass, self.push_button_login)
        LoginForm.setTabOrder(self.push_button_login, self.push_button_register)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.label.setText(_translate("LoginForm", "Logowanie"))
        self.label_login.setText(_translate("LoginForm", "Login"))
        self.label_pass.setText(_translate("LoginForm", "Hasło"))
        self.push_button_register.setText(_translate("LoginForm", "Rejestracja"))
        self.push_button_login.setText(_translate("LoginForm", "Zaloguj"))

