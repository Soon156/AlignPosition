# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from UI import resource_rc


class Ui_quick_access_dialog(object):
    def setupUi(self, quick_access_dialog):
        if not quick_access_dialog.objectName():
            quick_access_dialog.setObjectName(u"quick_access_dialog")
        quick_access_dialog.resize(352, 416)
        icon = QIcon()
        icon.addFile(u":/newPrefix/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        quick_access_dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(quick_access_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(quick_access_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.start_box = QCheckBox(self.frame_7)
        self.start_box.setObjectName(u"start_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_box.sizePolicy().hasHeightForWidth())
        self.start_box.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.start_box)

        self.background_box = QCheckBox(self.frame_7)
        self.background_box.setObjectName(u"background_box")
        sizePolicy1.setHeightForWidth(self.background_box.sizePolicy().hasHeightForWidth())
        self.background_box.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.background_box)


        self.verticalLayout.addWidget(self.frame_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.reminder_lbl = QLabel(self.frame_8)
        self.reminder_lbl.setObjectName(u"reminder_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.reminder_lbl.sizePolicy().hasHeightForWidth())
        self.reminder_lbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.reminder_lbl)

        self.reminder_box = QDoubleSpinBox(self.frame_8)
        self.reminder_box.setObjectName(u"reminder_box")

        self.horizontalLayout_6.addWidget(self.reminder_box)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.notify_box = QCheckBox(self.frame_9)
        self.notify_box.setObjectName(u"notify_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.notify_box.sizePolicy().hasHeightForWidth())
        self.notify_box.setSizePolicy(sizePolicy3)

        self.verticalLayout_5.addWidget(self.notify_box)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.alert_lbl = QLabel(self.frame_6)
        self.alert_lbl.setObjectName(u"alert_lbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.alert_lbl.sizePolicy().hasHeightForWidth())
        self.alert_lbl.setSizePolicy(sizePolicy4)
        self.alert_lbl.setBaseSize(QSize(1, 0))
        self.alert_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.alert_lbl)

        self.alert_box = QComboBox(self.frame_6)
        self.alert_box.setObjectName(u"alert_box")
        sizePolicy.setHeightForWidth(self.alert_box.sizePolicy().hasHeightForWidth())
        self.alert_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.alert_box)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.camera_lbl = QLabel(self.frame_5)
        self.camera_lbl.setObjectName(u"camera_lbl")
        self.camera_lbl.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.camera_lbl.sizePolicy().hasHeightForWidth())
        self.camera_lbl.setSizePolicy(sizePolicy4)
        self.camera_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.camera_lbl)

        self.camera_box = QComboBox(self.frame_5)
        self.camera_box.setObjectName(u"camera_box")
        sizePolicy.setHeightForWidth(self.camera_box.sizePolicy().hasHeightForWidth())
        self.camera_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.camera_box)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calibrate_btn = QPushButton(self.frame_2)
        self.calibrate_btn.setObjectName(u"calibrate_btn")

        self.horizontalLayout.addWidget(self.calibrate_btn)

        self.reset_btn = QPushButton(self.frame_2)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout.addWidget(self.reset_btn)

        self.apply_btn = QPushButton(self.frame_2)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout.addWidget(self.apply_btn)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(quick_access_dialog)

        QMetaObject.connectSlotsByName(quick_access_dialog)
    # setupUi

    def retranslateUi(self, quick_access_dialog):
        quick_access_dialog.setWindowTitle(QCoreApplication.translate("quick_access_dialog", u"Settings", None))
        self.start_box.setText(QCoreApplication.translate("quick_access_dialog", u"Auto Start", None))
        self.background_box.setText(QCoreApplication.translate("quick_access_dialog", u"Run In Background", None))
        self.reminder_lbl.setText(QCoreApplication.translate("quick_access_dialog", u"Break Time", None))
        self.notify_box.setText(QCoreApplication.translate("quick_access_dialog", u"Break Alert", None))
        self.alert_lbl.setText(QCoreApplication.translate("quick_access_dialog", u"Alert Position", None))
        self.camera_lbl.setText(QCoreApplication.translate("quick_access_dialog", u"Camera", None))
        self.calibrate_btn.setText(QCoreApplication.translate("quick_access_dialog", u"Calibrate", None))
        self.reset_btn.setText(QCoreApplication.translate("quick_access_dialog", u"Reset", None))
        self.apply_btn.setText(QCoreApplication.translate("quick_access_dialog", u"Apply", None))
    # retranslateUi

