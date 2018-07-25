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

from PyQt5.QtCore import pyqtSignal

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QEventLoop



class InteractionDialog(InteractionWrappedUI):

    callAnswerSignal = pyqtSignal(bool, str)

    def __init__(self, client):
        super(InteractionDialog, self).__init__()

        self.set_label_accept_pixmap("call-in-progress.png")
        self.set_label_reject_pixmap("call-ended.png")

        self.set_push_button_accept(self.accept_connection_clicked)
        self.set_push_button_reject(self.reject_connection_clicked)

        self.client = client
        self.userName = None
        self.userName_ip = None
        self.loop = QEventLoop()



    def setupCallerName(self, user_name : str):
        self.userName = user_name
        self.set_user_call_text(self.userName)

    def showCallerName(self, user_name : str):
        self.userName = user_name
        self.set_call_text(self.userName)



    def reject_connection_clicked(self):
        print("(*) InteractionDialog info: Not answer the call.")
        self.client.reject_connection(self.userName)
        self.callAnswerSignal.emit(False, self.userName)
        print("(*) InteractionDialog info: callAnswerSignal emited with False.")
        self.close()


    def accept_connection_clicked(self):
        print("(*) InteractionDialog info: Answer the call.")
        self.client.answer_call(self.userName)

        self.callAnswerSignal.emit(True, self.userName)
        self.push_button_accept.setEnabled(False)
        print("(*) InteractionDialog info: push_button_accept disabled.")
        print("(*) InteractionDialog info: callAnswerSignal emited with True.")


"""
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = InteractionWidget("Maciek")
    window.show()
    sys.exit(app.exec_())
"""
