# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JaroEliCall(object):
    def setupUi(self, JaroEliCall):
        JaroEliCall.setObjectName("JaroEliCall")
        JaroEliCall.resize(400, 300)
        self.login_Label = QtWidgets.QLabel(JaroEliCall)
        self.login_Label.setGeometry(QtCore.QRect(70, 80, 47, 13))
        self.login_Label.setObjectName("login_Label")
        self.password_Label = QtWidgets.QLabel(JaroEliCall)
        self.password_Label.setGeometry(QtCore.QRect(70, 130, 47, 13))
        self.password_Label.setObjectName("password_Label")
        self.login_VALUE = QtWidgets.QLineEdit(JaroEliCall)
        self.login_VALUE.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.login_VALUE.setObjectName("login_VALUE")
        self.password_VALUE = QtWidgets.QLineEdit(JaroEliCall)
        self.password_VALUE.setGeometry(QtCore.QRect(140, 130, 113, 20))
        self.password_VALUE.setObjectName("password_VALUE")
        self.register_button = QtWidgets.QPushButton(JaroEliCall)
        self.register_button.setGeometry(QtCore.QRect(60, 210, 91, 31))
        self.register_button.setObjectName("register_button")
        self.login_button = QtWidgets.QPushButton(JaroEliCall)
        self.login_button.setGeometry(QtCore.QRect(200, 210, 91, 31))
        self.login_button.setObjectName("login_button")

        self.retranslateUi(JaroEliCall)
        QtCore.QMetaObject.connectSlotsByName(JaroEliCall)

    def retranslateUi(self, JaroEliCall):
        _translate = QtCore.QCoreApplication.translate
        JaroEliCall.setWindowTitle(_translate("JaroEliCall", "Dialog"))
        self.login_Label.setText(_translate("JaroEliCall", "Login"))
        self.password_Label.setText(_translate("JaroEliCall", "Hasło"))
        self.register_button.setText(_translate("JaroEliCall", "Zarejestruj się"))
        self.login_button.setText(_translate("JaroEliCall", "Zaloguj się"))

