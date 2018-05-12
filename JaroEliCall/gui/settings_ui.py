# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.setWindowModality(QtCore.Qt.WindowModal)
        SettingsDialog.resize(370, 290)
        SettingsDialog.setMinimumSize(QtCore.QSize(370, 290))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sound = QtWidgets.QWidget()
        self.tab_sound.setObjectName("tab_sound")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_sound)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_sound)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.slider_speakers = QtWidgets.QSlider(self.tab_sound)
        self.slider_speakers.setOrientation(QtCore.Qt.Horizontal)
        self.slider_speakers.setObjectName("slider_speakers")
        self.verticalLayout_2.addWidget(self.slider_speakers)
        self.label_9 = QtWidgets.QLabel(self.tab_sound)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.slider_microphone = QtWidgets.QSlider(self.tab_sound)
        self.slider_microphone.setOrientation(QtCore.Qt.Horizontal)
        self.slider_microphone.setObjectName("slider_microphone")
        self.verticalLayout_2.addWidget(self.slider_microphone)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_sound)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_6.addWidget(self.checkBox_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_sound)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.tab_sound)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_sound)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab_sound)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.tabWidget.addTab(self.tab_sound, "")
        self.tab_profile = QtWidgets.QWidget()
        self.tab_profile.setObjectName("tab_profile")
        self.tabWidget.addTab(self.tab_profile, "")
        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Ustawienia"))
        self.label_8.setText(_translate("SettingsDialog", "Głośniki"))
        self.label_9.setText(_translate("SettingsDialog", "Mikrofon"))
        self.checkBox_2.setText(_translate("SettingsDialog", "Nagrywanie \n"
"gdy wciśnięto klawisz"))
        self.checkBox.setText(_translate("SettingsDialog", "Włącz/wyłącz \n"
"nagrywanie na przycisk"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sound), _translate("SettingsDialog", "Dźwięk"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profile), _translate("SettingsDialog", "Profil"))

