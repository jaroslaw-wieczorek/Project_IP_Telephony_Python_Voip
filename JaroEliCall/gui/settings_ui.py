# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Project_IP_Telephony_Python_Voip/JaroEliCall/gui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 292)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
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
