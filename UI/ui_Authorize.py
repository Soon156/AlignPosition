# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Authorize.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from UI import resource_rc


class Ui_Auth_Dialog(object):
    def setupUi(self, Auth_Dialog):
        if not Auth_Dialog.objectName():
            Auth_Dialog.setObjectName(u"Auth_Dialog")
        Auth_Dialog.resize(280, 126)
        icon = QIcon()
        icon.addFile(u":/newPrefix/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Auth_Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Auth_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Auth_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Auth_Dialog)

        QMetaObject.connectSlotsByName(Auth_Dialog)
    # setupUi

    def retranslateUi(self, Auth_Dialog):
        Auth_Dialog.setWindowTitle(QCoreApplication.translate("Auth_Dialog", u"Authorize", None))
        self.label.setText(QCoreApplication.translate("Auth_Dialog", u"Enter your 6-digit PIN", None))
        self.pushButton.setText(QCoreApplication.translate("Auth_Dialog", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("Auth_Dialog", u"TextLabel", None))
    # retranslateUi

