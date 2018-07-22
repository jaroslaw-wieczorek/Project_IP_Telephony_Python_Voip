import os
import sys
import json

from functools import partial
from threading import Thread


from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap 

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QMetaType
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QItemSelection

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

#(QItemSelection)
#self.emit(SIGNAL("newStatuses(PyQt_PyObject)"), statusy) 

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..','..'))
sys.path.append(lib_path2)


from JaroEliCall.src.client import Client
from JaroEliCall.src.wrapped_interfaces.main_wrapped_ui import MainWrappedUI

from JaroEliCall.src.class_between_threads import ClassBetweenThreads


class MainWindowDialog(MainWrappedUI):
    
    # Signal used when user close app after clicked esc or cros to close app.
    # If user clicked Yes on message box return True other way return False. 
   
    closingSignal = pyqtSignal(bool)
    callSignal = pyqtSignal(bool, str)
    
    def __init__(self, client):
        super(MainWindowDialog, self).__init__()
                
        self.client = client
        #self.__session_id = None
        
        self.username = self.setUserName(self.client.username)
        self.set_push_button_logout(partial(self.closeApp, "Uwaga!", "Czy napewno chesz się wylogować?"))
        
        #self.getList()
        
    def setUserName(self, user_name):
        self.username = user_name
        
    
    def getList(self):
        payload = {"type": "d", "description": "GET"}
        data = json.dumps(payload).encode("utf-8")
        print("{*} MainWindow info : Sended data to server:", data)
        self.client.sendMessage(data)

        #with self.client.lock:
        #self.client.listeningServer(self.client.
        self.read()


    def read(self):
        print("{*} MainWindow getting from Server : ", self.client.received)
        
        if(self.client.received == "202 USERS"):
            print("{*} MainWindow users: ", self.client.users)
            self.add_row_to_list_of_users(self.client.users)
            
        
    def keyPressEvent(self, event):
        """
            Close application from escape key.
        """
        if event.key() == Qt.Key_Escape:
            title = "Uwaga!"
            message = "Wyjście spowoduje automatyczne wylogowanie z aplikacji"
        
            self.closeApp(title, message)


    def closeApp(self, title, message):
        
        if QMessageBox.question(self, title, message) == QMessageBox.Yes:
            print("[*] MainWindowDialog info: Button Yes was clicked")
            self.closingSignal.emit(True)      
            self.client.closeConnection()
        else:
            print("[*] MainWindowDialog info: Button No was clicked")
            self.closingSignal.emit(False)


    
"""     List of contacts Widget
    Screen to load contacts and call to people
    __init__ - get list of people to table
    logout - logout   
    menu_rooms - going to list of available rooms
    call - call to person/people
"""

"""

class MainWindowDialog(MainWrappedUI):

    #sig = pyqtSignal(int)
    
    def __init__(self, client, toThread, login):
        super(MainWiFalsendowDialog, self).__init__()
        self.c = client
        self.closeEvent = self.notify
        self.client.= toThread
        self.getList()
        
        #self.login = login is not used ? 
        self.login = "jaro"
        
        # wait_for_conn = Thread(target=self.wait_for_calling, args=[self.client.])
        # wait_for_conn.start()

        # podpięcie metod z AddUserWidget do przycisków interfejsu
        self.set_push_button_logout(self.logout)
        self.set_push_button_invite(self.menu_rooms)
        self.set_push_button_call(self.call)

        # poszerzenie kolumn tabeli do szerokości widżetu
        self.set_fit_width()
        self.my_username = client.username
        

    def wait_for_calling(self, toThread):
        with self.client.lock:
            self.c.listening(toThread)
            self.read()
            

    def read(self):
        print(self.client.received)
        print("Odczytalem ", self.client.received)
        
        if(self.client.received[-1] == "202 USERS"):
            print("Userzy: ", self.client.users)
            self.add_row_to_list_of_users(self.client.users)
            
        if(self.client.received[-1] == "406 INVITE"):
            self.set_info_text("Nie można polaczyc sie z klientem")
            self.show_info_text()
            
        if(self.client.received[-1] == "200 LOGOUT"):
            self.close()
            
        if(self.client.received[-1][0:10]=="200 CALLING"):
            print("Dostalem: ", self.client.received[-1])
            
            # Potrzebne komentarze co tu się dzieje 
            data = self.client.received[-1][11::].replace('[','(')
            ip_and_port = data.replace(']',')')
            ip = str(ip_and_port[ip_and_port.find("'")+len("'"):ip_and_port.rfind("'")])
            port = int(ip_and_port[ip_and_port.find(" ")+len(" "):ip_and_port.rfind(")")])

            payload = {"type": "d", "status": "TO_YOU", 
                       "description": "INVITE", "who": self.my_username}
           
            data = json.dumps(payload).encode("utf-8")
            listening_client = Thread(target=self.c.listening_all, args= [port,])
            listening_client.start()

            self.c.sendMessage_another_client(data, port)

            print("Wysłano INVITE do " + str(ip) + " " + str(port))


    def getList(self):
        payload = {"type": "d", "description": "GET"}
        data = json.dumps(payload).encode("utf-8")
        print("Wysłano do serwera:", data)
        self.c.sendMessage(data)

        self.client.= betweenTherads.ClassBetweenhreads()

        with self.client.lock:
            self.c.listening(self.client.
            self.read()


    def updateMongo(self):
        payload = {"type": "d", "description": "LOGOUT"}
        data = json.dumps(payload).encode("utf-8")
        print(data)
        self.c.sendMessage(data)


    #@pyqtSlot()
    def logout(self):
        print("Wylogowanie")
        self.updateMongo()
        self.hide()


    #@pyqtSlot()
    def menu_rooms(self):
        print("Jestem u siebie")


    #@pyqtSlot()
    def call(self):
        where = self.table_widget_list_of_users.currentItem().text()
        if(where != ''):
            print("Wybrano dzwonienie do ", where)
            payload = {"type": "d", "description": "INVITE", "call_to": where}
            data = json.dumps(payload).encode("utf-8")
            print(data)
            self.c.sendMessage(data)

            with self.client.lock:
                self.c.listening(self.client.
                self.read()


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
    window = MainWindowDialog(" ")
  
    window.show()
    sys.exit(app.exec_())
"""