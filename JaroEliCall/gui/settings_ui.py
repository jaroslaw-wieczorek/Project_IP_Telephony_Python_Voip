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
        SettingsDialog.setMaximumSize(QtCore.QSize(370, 290))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab_widget = QtWidgets.QTabWidget(SettingsDialog)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_sound = QtWidgets.QWidget()
        self.tab_sound.setObjectName("tab_sound")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_sound)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.label_speakers = QtWidgets.QLabel(self.tab_sound)
        self.label_speakers.setObjectName("label_speakers")
        self.vertical_layout_1.addWidget(self.label_speakers)
        self.slider_speakers = QtWidgets.QSlider(self.tab_sound)
        self.slider_speakers.setOrientation(QtCore.Qt.Horizontal)
        self.slider_speakers.setObjectName("slider_speakers")
        self.vertical_layout_1.addWidget(self.slider_speakers)
        self.label_microphone = QtWidgets.QLabel(self.tab_sound)
        self.label_microphone.setObjectName("label_microphone")
        self.vertical_layout_1.addWidget(self.label_microphone)
        self.slider_microphone = QtWidgets.QSlider(self.tab_sound)
        self.slider_microphone.setOrientation(QtCore.Qt.Horizontal)
        self.slider_microphone.setObjectName("slider_microphone")
        self.vertical_layout_1.addWidget(self.slider_microphone)
        self.verticalLayout.addLayout(self.vertical_layout_1)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.check_box_record_when_button_pressed = QtWidgets.QCheckBox(self.tab_sound)
        self.check_box_record_when_button_pressed.setObjectName("check_box_record_when_button_pressed")
        self.horizontal_layout_1.addWidget(self.check_box_record_when_button_pressed)
        self.line_edit_button = QtWidgets.QLineEdit(self.tab_sound)
        self.line_edit_button.setObjectName("line_edit_button")
        self.horizontal_layout_1.addWidget(self.line_edit_button)
        self.verticalLayout.addLayout(self.horizontal_layout_1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab_sound)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.tab_widget.addTab(self.tab_sound, "")
        self.tab_profile = QtWidgets.QWidget()
        self.tab_profile.setObjectName("tab_profile")
        self.tab_widget.addTab(self.tab_profile, "")
        self.verticalLayout_3.addWidget(self.tab_widget)

        self.retranslateUi(SettingsDialog)
        self.tab_widget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Ustawienia"))
        self.label_speakers.setText(_translate("SettingsDialog", "Głośniki"))
        self.label_microphone.setText(_translate("SettingsDialog", "Mikrofon"))
        self.check_box_record_when_button_pressed.setText(_translate("SettingsDialog", "Nagrywanie \n"
"gdy wciśnięto klawisz"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_sound), _translate("SettingsDialog", "Dźwięk"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_profile), _translate("SettingsDialog", "Profil"))

