import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.MainWindow import Ui_MainWindow

from about import AboutDialog
from mail_servers import MailServersWindow
from preferences import PreferencesWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    servers_window = None
    preferences_window = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_Quit.triggered.connect(self.quit)
        self.action_Mail_Servers.triggered.connect(self.show_mail_servers_window)
        self.action_Preferences.triggered.connect(self.show_preferences_window)
        self.action_About.triggered.connect(self.about_dialog)

    def about_dialog(self):
        about = AboutDialog()
        about.exec()

    def show_mail_servers_window(self):
        if not self.servers_window:
            self.servers_window = MailServersWindow()
        self.servers_window.show()

    def show_preferences_window(self):
        if not self.preferences_window:
            self.preferences_window = PreferencesWindow()
        self.preferences_window.show()

    def quit(self):
        # TODO: add a confirmation request?
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
