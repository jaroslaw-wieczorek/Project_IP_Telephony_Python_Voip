import os
import sys
from threading import Thread

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path2)

from src.wrapped_interfaces.interaction_wrapped_ui import InteractionWrappedUI


class InteractionDialog(InteractionWrappedUI):

    callAnswerSignal = pyqtSignal(bool, str)

    endCallSignal = pyqtSignal(bool)

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

        self.is_connection_begin = False

    def setupCallerName(self, user_name):
        self.userName = user_name
        self.set_user_call_text(self.userName)

    def setupCallerAvatar(self, user_name):

        avatar_name = self.client.get_avatar(user_name)
        pixmap = QPixmap('gui/resources/avatars/' + str(avatar_name))
        self.label_avatar.setPixmap(pixmap)

    def showCallerName(self, user_name):
        self.userName = user_name
        self.set_call_text(self.userName)

    def reject_connection_clicked(self):
        if self.is_connection_begin is False:
            print("Polaczenie zostalo odrzucone")
            print("(*) InteractionDialog info: Not answer the call.")

            self.client.reject_connection(self.userName)
            self.callAnswerSignal.emit(False, self.userName)
            print("(*) InteractionDialog info: callAnswerSignal " +
                  "emited with False.")

            self.close()

        elif self.is_connection_begin is True:
            print("Polaczenie zostalo zakonczone")
            self.client.send_end_connection(self.userName)
            self.endCallSignal.emit(True)
            self.client.end_connection()

            self.close()

    def accept_connection_clicked(self):
        print("(*) InteractionDialog info: Answer the call.")
        self.client.answer_call(self.userName)
        self.client.voice(self.client.from_who_ip, 9998, 9999)

        self.callAnswerSignal.emit(True, self.userName)
        self.push_button_accept.setEnabled(False)

        self.is_connection_begin = True
        print("(*) InteractionDialog info: push_button_accept disabled.")
        print("(*) InteractionDialog info: callAnswerSignal emited with True.")


"""
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = InteractionWidget("Maciek")
    window.show()
    sys.exit(app.exec_())
"""
