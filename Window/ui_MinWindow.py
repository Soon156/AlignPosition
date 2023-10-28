# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MinWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
import resource_rc

class Ui_minDialog(object):
    def setupUi(self, minDialog):
        if not minDialog.objectName():
            minDialog.setObjectName(u"minDialog")
        minDialog.resize(194, 47)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        minDialog.setWindowIcon(icon)
        minDialog.setStyleSheet(u"#minDialog {background-color: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 rgb(26, 16, 57), stop:0.5 rgb(41, 14, 47), stop:1 rgb(26, 16, 57))}\n"
"")
        self.horizontalLayout = QHBoxLayout(minDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.use_time_lbl = QLabel(minDialog)
        self.use_time_lbl.setObjectName(u"use_time_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_time_lbl.sizePolicy().hasHeightForWidth())
        self.use_time_lbl.setSizePolicy(sizePolicy)
        self.use_time_lbl.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.use_time_lbl.setFont(font)
        self.use_time_lbl.setStyleSheet(u"color: white;\n"
"font-family: \"Roboto\", sans-serif;")
        self.use_time_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.use_time_lbl, 0, Qt.AlignVCenter)

        self.stop_btn = QPushButton(minDialog)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setStyleSheet(u"background: transparent;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons8-stop-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.stop_btn)

        self.start_btn = QPushButton(minDialog)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setStyleSheet(u"background: transparent;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons8-play-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.start_btn)

        self.close_btn = QPushButton(minDialog)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"background: transparent;\n"
"")
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

