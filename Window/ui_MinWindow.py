# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MinWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import Window.resource_rc

class Ui_minDialog(object):
    def setupUi(self, minDialog):
        if not minDialog.objectName():
            minDialog.setObjectName(u"minDialog")
        minDialog.resize(183, 46)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        minDialog.setWindowIcon(icon)
        minDialog.setStyleSheet(u"background-color: rgb(0, 28, 48);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(minDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.use_time_lbl = QLabel(minDialog)
        self.use_time_lbl.setObjectName(u"use_time_lbl")
        font = QFont()
        font.setPointSize(12)
        self.use_time_lbl.setFont(font)
        self.use_time_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.use_time_lbl, 0, Qt.AlignVCenter)

        self.stop_btn = QPushButton(minDialog)
        self.stop_btn.setObjectName(u"stop_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons8-stop-48 (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.stop_btn)

        self.start_btn = QPushButton(minDialog)
        self.start_btn.setObjectName(u"start_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons8-play-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.start_btn)

        self.close_btn = QPushButton(minDialog)
        self.close_btn.setObjectName(u"close_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons8-close-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.close_btn)


        self.retranslateUi(minDialog)

        QMetaObject.connectSlotsByName(minDialog)
    # setupUi

    def retranslateUi(self, minDialog):
        minDialog.setWindowTitle(QCoreApplication.translate("minDialog", u"Align Position", None))
        self.use_time_lbl.setText(QCoreApplication.translate("minDialog", u"00:00:00", None))
        self.stop_btn.setText("")
        self.start_btn.setText("")
        self.close_btn.setText("")
    # retranslateUi

