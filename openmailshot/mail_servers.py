import pickle

from PySide6.QtWidgets import QMainWindow

from models.mail_servers import MailServerConfigs
from ui.MailServersWindow import Ui_MailServersWindow


class MailServersWindow(QMainWindow, Ui_MailServersWindow):

    def __init__(self):
        super(MailServersWindow, self).__init__()
        self.setupUi(self)
        self.model = MailServerConfigs()
        self.load()
        self.mailserverView.setModel(self.model)
        self.newButton.pressed.connect(self.new)
        self.deleteButton.pressed.connect(self.delete)
        self.nameEdit.textChanged.connect(self.check_save_cancel)
        self.saveButton.pressed.connect(self.save)
        self.cancelButton.pressed.connect(self.cancel)
        self.mailserverView.clicked.connect(self.select_config)

    def enable_config_fields(self):
        self.nameLabel.setDisabled(False)
        self.nameEdit.setDisabled(False)
        self.configBox.setDisabled(False)
        self.newButton.setDisabled(True)

    def check_save_cancel(self):
        if self.nameEdit.text():
            self.saveButton.setDisabled(False)
            self.cancelButton.setDisabled(False)
        else:
            self.saveButton.setDisabled(True)
            self.cancelButton.setDisabled(True)

    def disable_config_fields(self):
        self.nameLabel.setDisabled(True)
        self.nameEdit.setDisabled(True)
        self.configBox.setDisabled(True)
        self.saveButton.setDisabled(True)
        self.cancelButton.setDisabled(True)

    def clear_fields(self):
        self.nameEdit.setText('')
        self.hostEdit.setText('')
        self.portEdit.setText('')
        self.userEdit.setText('')
        self.passEdit.setText('')
        self.notesEdit.setText('')

    def clear_selection(self):
        self.mailserverView.clearSelection()
        self.clear_fields()
        self.disable_config_fields()
        self.newButton.setDisabled(False)
        self.deleteButton.setDisabled(True)

    def select_config(self, index):
        config = self.model.configs[index.row()]
        self.nameEdit.setText(config['name'])
        self.hostEdit.setText(config['host'])
        self.portEdit.setText(config['port'])
        self.userEdit.setText(config['user'])
        self.passEdit.setText(config['pass'])
        self.notesEdit.setText(config['notes'])
        self.enable_config_fields()
        self.deleteButton.setDisabled(False)

    def load(self):
        try:
            with open('DATA/MAIL_SERVERS', 'rb') as f:
                self.model.configs = pickle.load(f)
        except Exception:
            pass

    def new(self):
        self.enable_config_fields()
        self.newButton.setDisabled(True)

    def save(self):
        name = self.nameEdit.text()
        hostname = self.hostEdit.text()
        port = self.portEdit.text()
        username = self.userEdit.text()
        password = self.passEdit.text()
        notes = self.notesEdit.toPlainText()
        config = {'name': name, 'host': hostname, 'port': port, 'user': username, 'pass': password, 'notes': notes}
        indexes = self.mailserverView.selectedIndexes()
        if indexes:
            index = indexes[0]
            self.model.configs[index.row()] = config
        else:
            self.model.configs.append(config)
        self.model.layoutChanged.emit()
        self.clear_selection()
        with open('DATA/MAIL_SERVERS', 'wb') as f:
            pickle.dump(self.model.configs, f)

    def cancel(self):
        self.clear_fields()
        self.clear_selection()
        self.disable_config_fields()

    def delete(self):
        indexes = self.mailserverView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.configs[index.row()]
            self.model.layoutChanged.emit()
            self.clear_selection()
            with open('DATA/MAIL_SERVERS', 'wb') as f:
                pickle.dump(self.model.configs, f)
