# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/ui/password_change.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginInterfaceDialog(object):
    def setupUi(self, LoginInterfaceDialog):
        LoginInterfaceDialog.setObjectName("LoginInterfaceDialog")
        LoginInterfaceDialog.resize(271, 247)
        LoginInterfaceDialog.setMinimumSize(QtCore.QSize(0, 0))
        LoginInterfaceDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginInterfaceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_form_name = QtWidgets.QLabel(LoginInterfaceDialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_form_name.setFont(font)
        self.label_form_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_form_name.setObjectName("label_form_name")
        self.verticalLayout.addWidget(self.label_form_name)
        spacerItem1 = QtWidgets.QSpacerItem(10, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label_info = QtWidgets.QLabel(LoginInterfaceDialog)
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.label_login = QtWidgets.QLabel(LoginInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy)
        self.label_login.setMinimumSize(QtCore.QSize(45, 0))
        self.label_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_login.setObjectName("label_login")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_login)
        self.line_edit_login = QtWidgets.QLineEdit(LoginInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_login.sizePolicy().hasHeightForWidth())
        self.line_edit_login.setSizePolicy(sizePolicy)
        self.line_edit_login.setMinimumSize(QtCore.QSize(50, 0))
        self.line_edit_login.setMaxLength(20)
        self.line_edit_login.setObjectName("line_edit_login")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_login)
        self.label_password = QtWidgets.QLabel(LoginInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)
        self.label_password.setMinimumSize(QtCore.QSize(45, 0))
        self.label_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.line_edit_password = QtWidgets.QLineEdit(LoginInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_password.sizePolicy().hasHeightForWidth())
        self.line_edit_password.setSizePolicy(sizePolicy)
        self.line_edit_password.setMinimumSize(QtCore.QSize(50, 0))
        self.line_edit_password.setMaxLength(20)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_edit_password)
        self.label_repeat_password = QtWidgets.QLabel(LoginInterfaceDialog)
        self.label_repeat_password.setObjectName("label_repeat_password")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_repeat_password)
        self.line_edit_repeat_password = QtWidgets.QLineEdit(LoginInterfaceDialog)
        self.line_edit_repeat_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_repeat_password.setObjectName("line_edit_repeat_password")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_edit_repeat_password)
        self.verticalLayout.addLayout(self.form_layout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_5.setSpacing(2)
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacerItem4)
        self.push_button_change_password = QtWidgets.QPushButton(LoginInterfaceDialog)
        self.push_button_change_password.setObjectName("push_button_change_password")
        self.horizontal_layout_5.addWidget(self.push_button_change_password)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontal_layout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(LoginInterfaceDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginInterfaceDialog)
        LoginInterfaceDialog.setTabOrder(self.line_edit_login, self.line_edit_password)
        LoginInterfaceDialog.setTabOrder(self.line_edit_password, self.push_button_change_password)

    def retranslateUi(self, LoginInterfaceDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginInterfaceDialog.setWindowTitle(_translate("LoginInterfaceDialog", "Dialog"))
        self.label_form_name.setText(_translate("LoginInterfaceDialog", "Zmiana hasła"))
        self.label_login.setText(_translate("LoginInterfaceDialog", "Login:"))
        self.label_password.setText(_translate("LoginInterfaceDialog", "Hasło:"))
        self.label_repeat_password.setText(_translate("LoginInterfaceDialog", "Powtórz hasło:"))
        self.push_button_change_password.setText(_translate("LoginInterfaceDialog", "Zmień hasło"))
