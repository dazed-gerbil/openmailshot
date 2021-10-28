import pickle

from PySide6.QtWidgets import QMainWindow

from ui.PreferencesWindow import Ui_PreferencesWindow


class PreferencesWindow(QMainWindow, Ui_PreferencesWindow):

    def __init__(self):
        super(PreferencesWindow, self).__init__()
        self.setupUi(self)
