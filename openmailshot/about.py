from PySide6.QtWidgets import QDialog

from ui.about import Ui_Dialog


class AboutDialog(QDialog, Ui_Dialog):

    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setupUi(self)
