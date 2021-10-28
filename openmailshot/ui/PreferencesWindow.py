# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreferencesWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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

class Ui_PreferencesWindow(object):
    def setupUi(self, PreferencesWindow):
        if not PreferencesWindow.objectName():
            PreferencesWindow.setObjectName(u"PreferencesWindow")
        PreferencesWindow.setWindowModality(Qt.ApplicationModal)
        PreferencesWindow.resize(800, 600)
        self.centralwidget = QWidget(PreferencesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        PreferencesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PreferencesWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        PreferencesWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PreferencesWindow)
        self.statusbar.setObjectName(u"statusbar")
        PreferencesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PreferencesWindow)

        QMetaObject.connectSlotsByName(PreferencesWindow)
    # setupUi

    def retranslateUi(self, PreferencesWindow):
        PreferencesWindow.setWindowTitle(QCoreApplication.translate("PreferencesWindow", u"Open Mail Shot Preferences", None))
    # retranslateUi

