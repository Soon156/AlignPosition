# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParentalSetting.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(219, 229)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"#Dialog {background-color: rgb(221, 242, 253);}\n"
"\n"
"QPushButton{\n"
"padding: 5px 20px 5px 20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ButtonFrame_2 = QFrame(Dialog)
        self.ButtonFrame_2.setObjectName(u"ButtonFrame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonFrame_2.sizePolicy().hasHeightForWidth())
        self.ButtonFrame_2.setSizePolicy(sizePolicy)
        self.ButtonFrame_2.setStyleSheet(u"font-family: \"Roboto\", sans-serif;\n"
"color: white;")
        self.ButtonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ButtonFrame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.monitor_setting_box = QCheckBox(self.ButtonFrame_2)
        self.monitor_setting_box.setObjectName(u"monitor_setting_box")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        self.monitor_setting_box.setFont(font)
        self.monitor_setting_box.setStyleSheet(u"QCheckBox {\n"
"	color:black;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/icons8-toggle-off-48.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/icons8-toggle-on-48.png);\n"
"}\n"
"\n"
"QToolTip {\n"
"background-color: white; \n"
"color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.monitor_setting_box)

        self.method_box = QCheckBox(self.ButtonFrame_2)
        self.method_box.setObjectName(u"method_box")
        self.method_box.setStyleSheet(u"QCheckBox {\n"
"	color:black;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/icons8-toggle-off-48.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/icons8-toggle-on-48.png);\n"
"}\n"
"\n"
"QToolTip {\n"
"background-color: white; \n"
"color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.method_box)

        self.reset_parental_btn = QPushButton(self.ButtonFrame_2)
        self.reset_parental_btn.setObjectName(u"reset_parental_btn")
        self.reset_parental_btn.setMinimumSize(QSize(150, 0))
        self.reset_parental_btn.setStyleSheet(u"QPushButton{\n"
"background-color: #a10000;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #d10000;\n"
"}")

        self.verticalLayout_2.addWidget(self.reset_parental_btn)

        self.restore_btn = QPushButton(self.ButtonFrame_2)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setEnabled(True)
        self.restore_btn.setMinimumSize(QSize(150, 0))
        self.restore_btn.setStyleSheet(u"QPushButton {background-color: #00d991;}\n"
"QPushButton:hover{background-color: #00fca8;}\n"
"QPushButton:pressed{background-color: #00fca8;}")

        self.verticalLayout_2.addWidget(self.restore_btn)

        self.exct_data_btn = QPushButton(self.ButtonFrame_2)
        self.exct_data_btn.setObjectName(u"exct_data_btn")
        self.exct_data_btn.setMinimumSize(QSize(150, 0))
        self.exct_data_btn.setStyleSheet(u"QPushButton{\n"
"background-color: #427D9D;\n"
"padding: 5px 20px 5px 20px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #9BBEC8;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.exct_data_btn)

        self.changePIN_btn = QPushButton(self.ButtonFrame_2)
        self.changePIN_btn.setObjectName(u"changePIN_btn")
        self.changePIN_btn.setMinimumSize(QSize(150, 0))
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
#if QT_CONFIG(tooltip)
        self.monitor_setting_box.setToolTip(QCoreApplication.translate("Dialog", u"Automatically start detection when application is opened", None))
#endif // QT_CONFIG(tooltip)
        self.monitor_setting_box.setText(QCoreApplication.translate("Dialog", u"Monitor", None))
#if QT_CONFIG(tooltip)
        self.method_box.setToolTip(QCoreApplication.translate("Dialog", u"Switch to able/disable posture detection", None))
#endif // QT_CONFIG(tooltip)
        self.method_box.setText(QCoreApplication.translate("Dialog", u"Detection", None))
        self.reset_parental_btn.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.restore_btn.setText(QCoreApplication.translate("Dialog", u"Restore Data", None))
        self.exct_data_btn.setText(QCoreApplication.translate("Dialog", u"Extract All Data", None))
        self.changePIN_btn.setText(QCoreApplication.translate("Dialog", u"Change PIN", None))
    # retranslateUi

