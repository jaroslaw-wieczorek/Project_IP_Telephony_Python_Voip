# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Dokumenty/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterInterfaceDialog(object):
    def setupUi(self, RegisterInterfaceDialog):
        RegisterInterfaceDialog.setObjectName("RegisterInterfaceDialog")
        RegisterInterfaceDialog.resize(310, 290)
        RegisterInterfaceDialog.setMinimumSize(QtCore.QSize(310, 290))
        RegisterInterfaceDialog.setMaximumSize(QtCore.QSize(310, 305))
        self.verticalLayout = QtWidgets.QVBoxLayout(RegisterInterfaceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_form_name = QtWidgets.QLabel(RegisterInterfaceDialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_form_name.setFont(font)
        self.label_form_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_form_name.setObjectName("label_form_name")
        self.verticalLayout.addWidget(self.label_form_name)
        spacerItem1 = QtWidgets.QSpacerItem(10, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.label_login = QtWidgets.QLabel(RegisterInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy)
        self.label_login.setMinimumSize(QtCore.QSize(90, 0))
        self.label_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_login.setObjectName("label_login")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_login)
        self.line_edit_login = QtWidgets.QLineEdit(RegisterInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_login.sizePolicy().hasHeightForWidth())
        self.line_edit_login.setSizePolicy(sizePolicy)
        self.line_edit_login.setMinimumSize(QtCore.QSize(50, 0))
        self.line_edit_login.setMaxLength(20)
        self.line_edit_login.setObjectName("line_edit_login")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_login)
        self.label_email = QtWidgets.QLabel(RegisterInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy)
        self.label_email.setMinimumSize(QtCore.QSize(90, 0))
        self.label_email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_email.setObjectName("label_email")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.line_edit_email = QtWidgets.QLineEdit(RegisterInterfaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_email.sizePolicy().hasHeightForWidth())
        self.line_edit_email.setSizePolicy(sizePolicy)
        self.line_edit_email.setMinimumSize(QtCore.QSize(50, 0))
        self.line_edit_email.setMaxLength(50)
        self.line_edit_email.setObjectName("line_edit_email")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_edit_email)
        self.label_password = QtWidgets.QLabel(RegisterInterfaceDialog)
        self.label_password.setMinimumSize(QtCore.QSize(90, 0))
        self.label_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.label_repeat_password = QtWidgets.QLabel(RegisterInterfaceDialog)
        self.label_repeat_password.setMinimumSize(QtCore.QSize(90, 0))
        self.label_repeat_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_repeat_password.setObjectName("label_repeat_password")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_repeat_password)
        self.line_edit_repeat_password = QtWidgets.QLineEdit(RegisterInterfaceDialog)
        self.line_edit_repeat_password.setMaxLength(20)
        self.line_edit_repeat_password.setObjectName("line_edit_repeat_password")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_edit_repeat_password)
        self.line_edit_password = QtWidgets.QLineEdit(RegisterInterfaceDialog)
        self.line_edit_password.setMaxLength(20)
        self.line_edit_password.setObjectName("line_edit_password")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_edit_password)
        self.verticalLayout.addLayout(self.form_layout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_5.setSpacing(2)
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacerItem3)
        self.push_button_register = QtWidgets.QPushButton(RegisterInterfaceDialog)
        self.push_button_register.setObjectName("push_button_register")
        self.horizontal_layout_5.addWidget(self.push_button_register)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacerItem4)
        self.push_button_already_account = QtWidgets.QPushButton(RegisterInterfaceDialog)
        self.push_button_already_account.setObjectName("push_button_already_account")
        self.horizontal_layout_5.addWidget(self.push_button_already_account)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontal_layout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(RegisterInterfaceDialog)
        QtCore.QMetaObject.connectSlotsByName(RegisterInterfaceDialog)

    def retranslateUi(self, RegisterInterfaceDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterInterfaceDialog.setWindowTitle(_translate("RegisterInterfaceDialog", "JaroEliCall  -  Rejestracja"))
        self.label_form_name.setText(_translate("RegisterInterfaceDialog", "Rejestracja użytkownika"))
        self.label_login.setText(_translate("RegisterInterfaceDialog", "Login:"))
        self.label_email.setText(_translate("RegisterInterfaceDialog", "E-mail:"))
        self.label_password.setText(_translate("RegisterInterfaceDialog", "Hasło"))
        self.label_repeat_password.setText(_translate("RegisterInterfaceDialog", "Powtórz hasło"))
        self.push_button_register.setText(_translate("RegisterInterfaceDialog", "Zarejestruj się"))
        self.push_button_already_account.setText(_translate("RegisterInterfaceDialog", "Mam już konto"))

