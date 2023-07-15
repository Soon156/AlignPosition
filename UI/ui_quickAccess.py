# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quickaccess.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QLabel, QPushButton, QSizePolicy,
    QWidget)
from UI import resource_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(236, 247)
        icon = QIcon()
        icon.addFile(u":/Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.calibrate_btn = QPushButton(Dialog)
        self.calibrate_btn.setObjectName(u"calibrate_btn")
        self.calibrate_btn.setGeometry(QRect(30, 190, 81, 24))
        self.background_box = QCheckBox(Dialog)
        self.background_box.setObjectName(u"background_box")
        self.background_box.setGeometry(QRect(70, 40, 101, 20))
        self.notify_box = QCheckBox(Dialog)
        self.notify_box.setObjectName(u"notify_box")
        self.notify_box.setGeometry(QRect(70, 20, 91, 20))
        self.camera_box = QComboBox(Dialog)
        self.camera_box.setObjectName(u"camera_box")
        self.camera_box.setGeometry(QRect(100, 150, 101, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_box.sizePolicy().hasHeightForWidth())
        self.camera_box.setSizePolicy(sizePolicy)
        self.reminder_lbl = QLabel(Dialog)
        self.reminder_lbl.setObjectName(u"reminder_lbl")
        self.reminder_lbl.setGeometry(QRect(40, 70, 91, 16))
        self.camera_lbl = QLabel(Dialog)
        self.camera_lbl.setObjectName(u"camera_lbl")
        self.camera_lbl.setGeometry(QRect(40, 150, 51, 16))
        self.reset_btn = QPushButton(Dialog)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(130, 190, 81, 24))
        self.idle_lbl = QLabel(Dialog)
        self.idle_lbl.setObjectName(u"idle_lbl")
        self.idle_lbl.setGeometry(QRect(40, 110, 51, 16))
        self.reminder_box = QDoubleSpinBox(Dialog)
        self.reminder_box.setObjectName(u"reminder_box")
        self.reminder_box.setGeometry(QRect(140, 70, 62, 22))
        self.idle_box = QDoubleSpinBox(Dialog)
        self.idle_box.setObjectName(u"idle_box")
        self.idle_box.setGeometry(QRect(140, 110, 62, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Quick Access", None))
        self.calibrate_btn.setText(QCoreApplication.translate("Dialog", u"Calibrate", None))
        self.background_box.setText(QCoreApplication.translate("Dialog", u"Background", None))
        self.notify_box.setText(QCoreApplication.translate("Dialog", u"Notification", None))
        self.reminder_lbl.setText(QCoreApplication.translate("Dialog", u"Break Reminder", None))
        self.camera_lbl.setText(QCoreApplication.translate("Dialog", u"Camera", None))
        self.reset_btn.setText(QCoreApplication.translate("Dialog", u"Reset Config", None))
        self.idle_lbl.setText(QCoreApplication.translate("Dialog", u"Idle", None))
    # retranslateUi

