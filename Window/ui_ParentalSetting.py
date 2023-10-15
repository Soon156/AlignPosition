# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParentalSetting.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(258, 198)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"#Dialog {background-color: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 rgb(26, 16, 57), stop:0.5 rgb(41, 14, 47), stop:1 rgb(26, 16, 57))}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ButtonFrame_2 = QFrame(Dialog)
        self.ButtonFrame_2.setObjectName(u"ButtonFrame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonFrame_2.sizePolicy().hasHeightForWidth())
        self.ButtonFrame_2.setSizePolicy(sizePolicy)
        self.ButtonFrame_2.setStyleSheet(u"color: white;\n"
"font-family: \"Roboto\", sans-serif;")
        self.ButtonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ButtonFrame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.reset_parental_btn = QPushButton(self.ButtonFrame_2)
        self.reset_parental_btn.setObjectName(u"reset_parental_btn")
        self.reset_parental_btn.setMinimumSize(QSize(130, 0))
        self.reset_parental_btn.setStyleSheet(u"QPushButton{\n"
"background-color: #a10000;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: #d10000;\n"
"}")

        self.verticalLayout_2.addWidget(self.reset_parental_btn)

        self.restore_btn = QPushButton(self.ButtonFrame_2)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setEnabled(True)
        self.restore_btn.setMinimumSize(QSize(130, 0))
        self.restore_btn.setStyleSheet(u"QPushButton {background-color: #00d991;}\n"
"QPushButton:hover{background-color: #00fca8;}\n"
"QPushButton:pressed{background-color: #00fca8;}")

        self.verticalLayout_2.addWidget(self.restore_btn)

        self.exct_data_btn = QPushButton(self.ButtonFrame_2)
        self.exct_data_btn.setObjectName(u"exct_data_btn")
        self.exct_data_btn.setMinimumSize(QSize(130, 0))
        self.exct_data_btn.setStyleSheet(u"QPushButton{\n"
"background-color: #3b006e;\n"
"padding: 5px 20px 5px 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #a200ff;\n"
"}")

        self.verticalLayout_2.addWidget(self.exct_data_btn)

        self.changePIN_btn = QPushButton(self.ButtonFrame_2)
        self.changePIN_btn.setObjectName(u"changePIN_btn")
        self.changePIN_btn.setMinimumSize(QSize(130, 0))
        self.changePIN_btn.setStyleSheet(u"QPushButton{\n"
"background-color: #3b006e;\n"
"padding: 5px 20px 5px 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #a200ff;\n"
"}")

        self.verticalLayout_2.addWidget(self.changePIN_btn)


        self.verticalLayout.addWidget(self.ButtonFrame_2, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Parental Settings", None))
        self.reset_parental_btn.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.restore_btn.setText(QCoreApplication.translate("Dialog", u"Restore Data", None))
        self.exct_data_btn.setText(QCoreApplication.translate("Dialog", u"Extract All Data", None))
        self.changePIN_btn.setText(QCoreApplication.translate("Dialog", u"Change PIN", None))
    # retranslateUi

