# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from UI import resource_rc


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(307, 332)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(8)
        MainMenu.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainMenu.setWindowIcon(icon)
        MainMenu.setStyleSheet(u"")
        MainMenu.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.usetime_lbl = QLabel(MainMenu)
        self.usetime_lbl.setObjectName(u"usetime_lbl")
        self.usetime_lbl.setGeometry(QRect(20, 140, 261, 28))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.usetime_lbl.setFont(font1)
        self.usetime_lbl.setContextMenuPolicy(Qt.NoContextMenu)
        self.usetime_lbl.setTextFormat(Qt.AutoText)
        self.usetime_lbl.setScaledContents(False)
        self.usetime_lbl.setAlignment(Qt.AlignCenter)
        self.usetime_lbl.setMargin(5)
        self.title_lbl = QLabel(MainMenu)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setGeometry(QRect(10, 40, 301, 101))
        self.title_lbl.setMaximumSize(QSize(16777215, 111))
        self.title_lbl.setPixmap(QPixmap(u":/Resources/Title.png"))
        self.title_lbl.setScaledContents(True)
        self.msg_label = QLabel(MainMenu)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setGeometry(QRect(50, 260, 191, 23))
        self.msg_label.setFont(font)
        self.msg_label.setContextMenuPolicy(Qt.NoContextMenu)
        self.msg_label.setTextFormat(Qt.AutoText)
        self.msg_label.setScaledContents(False)
        self.msg_label.setAlignment(Qt.AlignCenter)
        self.msg_label.setMargin(5)
        self.widget = QWidget(MainMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 170, 129, 89))
        self.quick_btn = QPushButton(self.widget)
        self.quick_btn.setObjectName(u"quick_btn")
        self.quick_btn.setGeometry(QRect(0, 60, 131, 24))
        self.quick_btn.setFont(font1)
        self.quick_btn.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(218, 255, 251);")
        self.start_btn = QPushButton(self.widget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(0, 0, 131, 24))
        self.start_btn.setFont(font1)
        self.start_btn.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(218, 255, 251);")
        self.parental_btn = QPushButton(self.widget)
        self.parental_btn.setObjectName(u"parental_btn")
        self.parental_btn.setGeometry(QRect(0, 30, 131, 24))
        self.parental_btn.setFont(font1)
        self.parental_btn.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(218, 255, 251);")

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"AlignPosition", None))
        self.usetime_lbl.setText(QCoreApplication.translate("MainMenu", u"TextLabel", None))
        self.title_lbl.setText("")
        self.msg_label.setText(QCoreApplication.translate("MainMenu", u"TextLabel", None))
        self.quick_btn.setText(QCoreApplication.translate("MainMenu", u"Quick Access", None))
        self.start_btn.setText(QCoreApplication.translate("MainMenu", u"Start Monitoring", None))
        self.parental_btn.setText(QCoreApplication.translate("MainMenu", u"Parental Control", None))
    # retranslateUi

