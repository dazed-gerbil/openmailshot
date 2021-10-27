import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.MainWindow import Ui_MainWindow

from about import AboutDialog
from mail_servers import MailServersWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    servers_window = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_Quit.triggered.connect(self.quit)
        self.action_Mail_Servers.triggered.connect(self.mail_servers_window)
        self.action_About.triggered.connect(self.about_dialog)

    def about_dialog(self):
        about = AboutDialog()
        about.exec()

    def mail_servers_window(self):
        if not self.servers_window:
            self.servers_window = MailServersWindow()
        self.servers_window.show()

    def quit(self):
        # TODO: add a confirmation request?
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
