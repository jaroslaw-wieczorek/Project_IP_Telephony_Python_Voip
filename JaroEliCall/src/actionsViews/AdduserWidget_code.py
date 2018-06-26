import os
import sys
import json
import threading
from threading import Thread

#(QItemSelection)
#self.emit(SIGNAL("newStatuses(PyQt_PyObject)"), statusy) 

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..','..'))
sys.path.append(lib_path2)

print(lib_path2)

from interface_management.adduser import AdduserDialog

from JaroEliCall.gui.adduser_ui import Ui_FormInterface

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap 

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QMetaType
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QItemSelection

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem


"""     List of contacts Widget
    Screen to load contacts and call to people
    __init__ - get list of people to table
    logout - logout   
    menu_rooms - going to list of available rooms
    call - call to person/people
"""

class AddUserWidget(AdduserDialog):

    #sig = pyqtSignal(int)
    
    def __init__(self, client):
        super(AddUserWidget, self).__init__()
        self.c = client
        self.closeEvent = self.notify
        #podpięcie metod z AddUserWidget do przycisków interfejsu
        self.set_push_button_logout(self.logout)
        self.set_push_button_invite(self.menu_rooms)
        self.set_push_button_call(self.call)

        #poszerzenie kolumn tabeli do szerokości widżetu
        self.set_fit_width()
    


    def updateMongo(self, user_ip):
        print(user_ip)
        payload = {"type": "d", "description": "LOGOUT"}

        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.sendMessage(data)

        self.close()

    #@pyqtSlot()
    def logout(self):
        print("Wylogowanie")
        self.updateMongo(self.c.host)

    #@pyqtSlot()
    def menu_rooms(self):
        pass

    #@pyqtSlot()
    def call(self):
        where = self.table_widget_list_of_users.currentItem().text()
        print("Wybrano dzwonienie do ", where)

    def notify(self, event):
        if self.close_event_message_box(event) == QMessageBox.Yes:
            self.logout()
            event.accept()
        else:
            event.ignore()
        
        #self.logout()
        print("notified")


# For tests   
if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = AddUserWidget(" ")
  
    window.show()
    sys.exit(app.exec_())
