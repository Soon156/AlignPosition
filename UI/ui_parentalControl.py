# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParentalControl.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
from UI import resource_rc


class Ui_ParentalControlDialog(object):
    def setupUi(self, ParentalControlDialog):
        if not ParentalControlDialog.objectName():
            ParentalControlDialog.setObjectName(u"ParentalControlDialog")
        ParentalControlDialog.resize(932, 475)
        icon = QIcon()
        icon.addFile(u":/newPrefix/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        ParentalControlDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(ParentalControlDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(ParentalControlDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QFont()
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tut_btn = QPushButton(self.frame)
        self.tut_btn.setObjectName(u"tut_btn")
        sizePolicy.setHeightForWidth(self.tut_btn.sizePolicy().hasHeightForWidth())
        self.tut_btn.setSizePolicy(sizePolicy)
        self.tut_btn.setMaximumSize(QSize(120, 25))
        self.tut_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.tut_btn)

        self.put_btn = QPushButton(self.frame)
        self.put_btn.setObjectName(u"put_btn")
        self.put_btn.setMaximumSize(QSize(120, 25))

        self.horizontalLayout.addWidget(self.put_btn)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout_3.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.tut_widget = QWidget()
        self.tut_widget.setObjectName(u"tut_widget")
        self.verticalLayout_4 = QVBoxLayout(self.tut_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tut_lbl = QLabel(self.tut_widget)
        self.tut_lbl.setObjectName(u"tut_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tut_lbl.sizePolicy().hasHeightForWidth())
        self.tut_lbl.setSizePolicy(sizePolicy2)
        self.tut_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.tut_lbl)

        self.tut_cont = QGridLayout()
        self.tut_cont.setObjectName(u"tut_cont")

        self.verticalLayout_4.addLayout(self.tut_cont)

        self.stackedWidget.addWidget(self.tut_widget)
        self.put_widget = QWidget()
        self.put_widget.setObjectName(u"put_widget")
        self.verticalLayout = QVBoxLayout(self.put_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.put_lbl = QLabel(self.put_widget)
        self.put_lbl.setObjectName(u"put_lbl")
        sizePolicy2.setHeightForWidth(self.put_lbl.sizePolicy().hasHeightForWidth())
        self.put_lbl.setSizePolicy(sizePolicy2)
        self.put_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.put_lbl)

        self.put_cont = QGridLayout()
        self.put_cont.setObjectName(u"put_cont")

        self.verticalLayout.addLayout(self.put_cont)

        self.stackedWidget.addWidget(self.put_widget)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.retranslateUi(ParentalControlDialog)

        self.tut_btn.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ParentalControlDialog)
    # setupUi

    def retranslateUi(self, ParentalControlDialog):
        ParentalControlDialog.setWindowTitle(QCoreApplication.translate("ParentalControlDialog", u"Parental Control", None))
        self.tut_btn.setText(QCoreApplication.translate("ParentalControlDialog", u"Total Use Time", None))
        self.put_btn.setText(QCoreApplication.translate("ParentalControlDialog", u"Program Use Time", None))
        self.checkBox.setText(QCoreApplication.translate("ParentalControlDialog", u" App Use Time Tracking", None))
        self.tut_lbl.setText(QCoreApplication.translate("ParentalControlDialog", u"tut_lbl", None))
        self.put_lbl.setText(QCoreApplication.translate("ParentalControlDialog", u"put_lbl", None))
    # retranslateUi

