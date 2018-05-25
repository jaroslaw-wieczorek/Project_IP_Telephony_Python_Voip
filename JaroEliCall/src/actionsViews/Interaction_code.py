from PyQt5.QtWidgets import QDialog
from JaroEliCall.gui.interaction_ui import Ui_Form
from PyQt5.QtCore import pyqtSlot


class InteractionWidget(QDialog, Ui_Form):
    def __init__(self, kto):
        super(InteractionWidget, self).__init__()
        self.setupUi(self)
        self.kto = kto
        self.label.setText("{0} dzwoni".format(kto))
        self.pushButton_3.clicked.connect(self.reject_connection_clicked)
        self.pushButton.clicked.connect(self.accept_connection_clicked)

    @pyqtSlot()
    def reject_connection_clicked(self):
        print("Odrzucono polaczenie")
        self.close()


    @pyqtSlot()
    def accept_connection_clicked(self):
        print("Odebrano połączenie")
        self.close()
