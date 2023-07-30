# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from UI import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 377)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.title_lbl = QLabel(self.frame)
        self.title_lbl.setObjectName(u"title_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_lbl.sizePolicy().hasHeightForWidth())
        self.title_lbl.setSizePolicy(sizePolicy1)
        self.title_lbl.setSizeIncrement(QSize(0, 0))
        self.title_lbl.setPixmap(QPixmap(u":/newPrefix/Small_title.png"))
        self.title_lbl.setScaledContents(True)
        self.title_lbl.setWordWrap(False)

        self.horizontalLayout.addWidget(self.title_lbl)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.frame)

        self.usetime_lbl = QLabel(self.centralwidget)
        self.usetime_lbl.setObjectName(u"usetime_lbl")
        sizePolicy.setHeightForWidth(self.usetime_lbl.sizePolicy().hasHeightForWidth())
        self.usetime_lbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.usetime_lbl.setFont(font)
        self.usetime_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.usetime_lbl)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.start_btn = QPushButton(self.frame_3)
        self.start_btn.setObjectName(u"start_btn")
        font1 = QFont()
        font1.setPointSize(12)
        self.start_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.start_btn)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.parental_btn = QPushButton(self.frame_4)
        self.parental_btn.setObjectName(u"parental_btn")
        self.parental_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.parental_btn)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.quick_btn = QPushButton(self.frame_5)
        self.quick_btn.setObjectName(u"quick_btn")
        self.quick_btn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.quick_btn)

        self.horizontalSpacer_6 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.msg_lbl = QLabel(self.centralwidget)
        self.msg_lbl.setObjectName(u"msg_lbl")
        sizePolicy.setHeightForWidth(self.msg_lbl.sizePolicy().hasHeightForWidth())
        self.msg_lbl.setSizePolicy(sizePolicy)
        self.msg_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.msg_lbl)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Align Position", None))
        self.title_lbl.setText("")
        self.usetime_lbl.setText(QCoreApplication.translate("MainWindow", u"Today Use Time : 0s", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start Monitoring", None))
        self.parental_btn.setText(QCoreApplication.translate("MainWindow", u"Parental Control", None))
        self.quick_btn.setText(QCoreApplication.translate("MainWindow", u"Quick Access", None))
        self.msg_lbl.setText(QCoreApplication.translate("MainWindow", u"Message of the day", None))
    # retranslateUi

