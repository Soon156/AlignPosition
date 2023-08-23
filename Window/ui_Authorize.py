# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Authorize.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_PINDialog(object):
    def setupUi(self, PINDialog):
        if not PINDialog.objectName():
            PINDialog.setObjectName(u"PINDialog")
        PINDialog.resize(229, 110)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        PINDialog.setWindowIcon(icon)
        PINDialog.setStyleSheet(u"#PINDialog {background-color: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 rgb(26, 16, 57), stop:0.5 rgb(41, 14, 47), stop:1 rgb(26, 16, 57))}")
        self.verticalLayout = QVBoxLayout(PINDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PINValidationFrame = QFrame(PINDialog)
        self.PINValidationFrame.setObjectName(u"PINValidationFrame")
        self.PINValidationFrame.setStyleSheet(u"color: white;\n"
"font-family: \"Roboto\", sans-serif;")
        self.PINValidationFrame.setFrameShape(QFrame.StyledPanel)
        self.PINValidationFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.PINValidationFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.PINValidationFrame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.PINFrame = QFrame(self.PINValidationFrame)
        self.PINFrame.setObjectName(u"PINFrame")
        self.PINFrame.setFrameShape(QFrame.StyledPanel)
        self.PINFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.PINFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.PIN_line = QLineEdit(self.PINFrame)
        self.PIN_line.setObjectName(u"PIN_line")
        self.PIN_line.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_7.addWidget(self.PIN_line)

        self.PIN_btn = QPushButton(self.PINFrame)
        self.PIN_btn.setObjectName(u"PIN_btn")
        self.PIN_btn.setStyleSheet(u"QPushButton{\n"
"padding: 3px 25px 3px 25px;\n"
"background-color: #00d991;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #00fca8;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.PIN_btn)


        self.verticalLayout_4.addWidget(self.PINFrame, 0, Qt.AlignVCenter)

        self.PIN_hint_lbl = QLabel(self.PINValidationFrame)
        self.PIN_hint_lbl.setObjectName(u"PIN_hint_lbl")
        sizePolicy.setHeightForWidth(self.PIN_hint_lbl.sizePolicy().hasHeightForWidth())
        self.PIN_hint_lbl.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.PIN_hint_lbl, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.PINValidationFrame, 0, Qt.AlignVCenter)


        self.retranslateUi(PINDialog)

        QMetaObject.connectSlotsByName(PINDialog)
    # setupUi

    def retranslateUi(self, PINDialog):
        PINDialog.setWindowTitle(QCoreApplication.translate("PINDialog", u"PIN", None))
        self.label.setText(QCoreApplication.translate("PINDialog", u"Enter your 6-digit PIN", None))
        self.PIN_btn.setText(QCoreApplication.translate("PINDialog", u"OK", None))
        self.PIN_hint_lbl.setText(QCoreApplication.translate("PINDialog", u"TextLabel", None))
    # retranslateUi

