import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)

lib_path2 = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path2)

from src.wrapped_interfaces.credits_wrapped_ui import CreditsWrappedUI


class CreditsDialog(CreditsWrappedUI):

	def __init__(self):
		super(CreditsDialog, self).__init__()
