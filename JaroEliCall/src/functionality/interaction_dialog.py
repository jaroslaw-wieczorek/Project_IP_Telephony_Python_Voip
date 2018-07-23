import os
import sys

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)


from src.wrapped_interfaces.interaction_wrapped_ui import InteractionWrappedUI

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap



class InteractionDialog(InteractionWrappedUI):
    def __init__(self, kto):
        super(InteractionDialog, self).__init__()

        self.kto = kto
        self.set_user_call_text("{0} dzwoni".format(kto))

        self.set_label_accept_pixmap("call-in-progress.png")
        self.set_label_reject_pixmap("call-ended.png")

        self.set_push_button_accept(self.accept_connection_clicked)
        self.set_push_button_reject(self.reject_connection_clicked)


    #@pyqtSlot()
    def reject_connection_clicked(self):
        print("Odrzucono polaczenie")
        self.close()


    #@pyqtSlot()
    def accept_connection_clicked(self):
        print("Odebrano połączenie")
        self.close()


"""
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = InteractionWidget("Maciek")
    window.show()
    sys.exit(app.exec_())
"""
