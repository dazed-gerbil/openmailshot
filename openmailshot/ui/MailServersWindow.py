# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MailServersWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MailServersWindow(object):
    def setupUi(self, MailServersWindow):
        if not MailServersWindow.objectName():
            MailServersWindow.setObjectName(u"MailServersWindow")
        MailServersWindow.setWindowModality(Qt.ApplicationModal)
        MailServersWindow.resize(800, 460)
        self.centralwidget = QWidget(MailServersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mailserverView = QListView(self.centralwidget)
        self.mailserverView.setObjectName(u"mailserverView")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailserverView.sizePolicy().hasHeightForWidth())
        self.mailserverView.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.mailserverView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newButton = QPushButton(self.centralwidget)
        self.newButton.setObjectName(u"newButton")

        self.horizontalLayout_2.addWidget(self.newButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nameEdit)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.configBox = QGroupBox(self.centralwidget)
        self.configBox.setObjectName(u"configBox")
        self.configBox.setEnabled(False)
        self.formLayout_3 = QFormLayout(self.configBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.configBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.hostEdit = QLineEdit(self.configBox)
        self.hostEdit.setObjectName(u"hostEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.hostEdit)

        self.label_3 = QLabel(self.configBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.portEdit = QLineEdit(self.configBox)
        self.portEdit.setObjectName(u"portEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.portEdit)

        self.label_4 = QLabel(self.configBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.userEdit = QLineEdit(self.configBox)
        self.userEdit.setObjectName(u"userEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.userEdit)

        self.passEdit = QLineEdit(self.configBox)
        self.passEdit.setObjectName(u"passEdit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.passEdit)

        self.label_5 = QLabel(self.configBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.configBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.notesEdit = QTextEdit(self.configBox)
        self.notesEdit.setObjectName(u"notesEdit")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.notesEdit)


        self.verticalLayout_2.addWidget(self.configBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MailServersWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MailServersWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MailServersWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MailServersWindow)
        self.statusbar.setObjectName(u"statusbar")
        MailServersWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.nameEdit, self.hostEdit)
        QWidget.setTabOrder(self.hostEdit, self.portEdit)
        QWidget.setTabOrder(self.portEdit, self.userEdit)
        QWidget.setTabOrder(self.userEdit, self.passEdit)
        QWidget.setTabOrder(self.passEdit, self.notesEdit)
        QWidget.setTabOrder(self.notesEdit, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.mailserverView)
        QWidget.setTabOrder(self.mailserverView, self.newButton)
        QWidget.setTabOrder(self.newButton, self.deleteButton)

        self.retranslateUi(MailServersWindow)

        QMetaObject.connectSlotsByName(MailServersWindow)
    # setupUi

    def retranslateUi(self, MailServersWindow):
        MailServersWindow.setWindowTitle(QCoreApplication.translate("MailServersWindow", u"Configure outgoing mail servers", None))
        self.newButton.setText(QCoreApplication.translate("MailServersWindow", u"New Mail Server", None))
        self.deleteButton.setText(QCoreApplication.translate("MailServersWindow", u"Delete Selected", None))
        self.nameLabel.setText(QCoreApplication.translate("MailServersWindow", u"Display name", None))
        self.configBox.setTitle(QCoreApplication.translate("MailServersWindow", u"Mail Server Configuration  ", None))
        self.label_2.setText(QCoreApplication.translate("MailServersWindow", u"Hostname", None))
        self.label_3.setText(QCoreApplication.translate("MailServersWindow", u"Port", None))
        self.label_4.setText(QCoreApplication.translate("MailServersWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("MailServersWindow", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("MailServersWindow", u"Notes", None))
        self.saveButton.setText(QCoreApplication.translate("MailServersWindow", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("MailServersWindow", u"Cancel", None))
    # retranslateUi

