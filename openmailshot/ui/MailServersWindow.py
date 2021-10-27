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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MailServersWindow(object):
    def setupUi(self, MailServersWindow):
        if not MailServersWindow.objectName():
            MailServersWindow.setObjectName(u"MailServersWindow")
        MailServersWindow.resize(800, 600)
        self.centralwidget = QWidget(MailServersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MailServersWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MailServersWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MailServersWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MailServersWindow)
        self.statusbar.setObjectName(u"statusbar")
        MailServersWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MailServersWindow)

        QMetaObject.connectSlotsByName(MailServersWindow)
    # setupUi

    def retranslateUi(self, MailServersWindow):
        MailServersWindow.setWindowTitle(QCoreApplication.translate("MailServersWindow", u"Configure outgoing mail servers", None))
    # retranslateUi

