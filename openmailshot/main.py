import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_Quit.triggered.connect(self.quit)

    def quit(self):
        # TODO: add a confirmation request?
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
