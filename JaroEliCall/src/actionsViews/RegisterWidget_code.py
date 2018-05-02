from PyQt5.QtWidgets import QDialog
from JaroEliCall.gui.register_ui import Ui_Form


#####   TO DO ####
"""     Register Widget
    Screen to Register
    register - on_reg_button_clicked = 
            * fulfilling gaps with data            
"""


class RegisterWidget(QDialog, Ui_Form):
    def __init__(self):
        super(RegisterWidget, self).__init__()
        self.setupUi(self)



