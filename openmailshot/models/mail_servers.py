from PySide6.QtCore import QAbstractListModel, Qt


class MailServerConfigs(QAbstractListModel):

    def __init__(self, configs=None):
        super(MailServerConfigs, self).__init__()
        self.configs = configs or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            display = self.configs[index.row()]
            return display['name']

    def rowCount(self, index):
        return len(self.configs)
