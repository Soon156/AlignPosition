# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibrate.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
from UI import resource_rc

class Ui_calibrate_win(object):
    def setupUi(self, calibrate_win):
        if not calibrate_win.objectName():
            calibrate_win.setObjectName(u"calibrate_win")
        calibrate_win.resize(388, 338)
        icon = QIcon()
        icon.addFile(u":/Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        calibrate_win.setWindowIcon(icon)
        self.hint_lbl = QLabel(calibrate_win)
        self.hint_lbl.setObjectName(u"hint_lbl")
        self.hint_lbl.setGeometry(QRect(40, 249, 301, 41))
        self.hint_lbl.setAlignment(Qt.AlignCenter)
        self.append_btn = QPushButton(calibrate_win)
        self.append_btn.setObjectName(u"append_btn")
        self.append_btn.setGeometry(QRect(250, 300, 101, 24))
        self.preview_lbl = QLabel(calibrate_win)
        self.preview_lbl.setObjectName(u"preview_lbl")
        self.preview_lbl.setGeometry(QRect(10, 10, 361, 221))
        self.calibrate_btn = QPushButton(calibrate_win)
        self.calibrate_btn.setObjectName(u"calibrate_btn")
        self.calibrate_btn.setGeometry(QRect(50, 300, 101, 24))
        self.proceed_btn = QPushButton(calibrate_win)
        self.proceed_btn.setObjectName(u"proceed_btn")
        self.proceed_btn.setEnabled(True)
        self.proceed_btn.setGeometry(QRect(60, 300, 81, 24))
        self.cancel_btn = QPushButton(calibrate_win)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(260, 300, 75, 24))
        self.calibrate_btn_2 = QPushButton(calibrate_win)
        self.calibrate_btn_2.setObjectName(u"calibrate_btn_2")
        self.calibrate_btn_2.setGeometry(QRect(150, 300, 101, 24))

        self.retranslateUi(calibrate_win)

        QMetaObject.connectSlotsByName(calibrate_win)
    # setupUi

    def retranslateUi(self, calibrate_win):
        calibrate_win.setWindowTitle(QCoreApplication.translate("calibrate_win", u"Calibration", None))
        self.hint_lbl.setText("")
        self.append_btn.setText(QCoreApplication.translate("calibrate_win", u"Add Bad Posture", None))
        self.preview_lbl.setText("")
        self.calibrate_btn.setText(QCoreApplication.translate("calibrate_win", u"Re-Calibrate", None))
        self.proceed_btn.setText(QCoreApplication.translate("calibrate_win", u"Proceed", None))
        self.cancel_btn.setText(QCoreApplication.translate("calibrate_win", u"Cancel", None))
        self.calibrate_btn_2.setText(QCoreApplication.translate("calibrate_win", u"Calibrate", None))
    # retranslateUi

