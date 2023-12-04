# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowDark.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 526)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#widget {background-color: qlineargradient(x1:0 y1:0, x2:0 y2:1, stop:0 rgb(26, 16, 57), stop:0.5 rgb(41, 14, 47), stop:1 rgb(26, 16, 57))}\n"
"QDoubleSpinBox {\n"
"	padding: 5px;\n"
"border: 1px solid #000;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    border-image: url(:/icon/icons8-up-48.png) 1;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    border-image: url(:/icon/icons8-down-48.png) 1;\n"
"}\n"
"QCheckBox {\n"
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
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"color: white;\n"
"font-family: \"Roboto\", sans-serif;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SideMenuBar = QFrame(self.widget)
        self.SideMenuBar.setObjectName(u"SideMenuBar")
        self.SideMenuBar.setStyleSheet(u"")
        self.SideMenuBar.setFrameShape(QFrame.StyledPanel)
        self.SideMenuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.SideMenuBar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 6, 6, 20)
        self.logo_with_title_lbl = QLabel(self.SideMenuBar)
        self.logo_with_title_lbl.setObjectName(u"logo_with_title_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_with_title_lbl.sizePolicy().hasHeightForWidth())
        self.logo_with_title_lbl.setSizePolicy(sizePolicy)
        self.logo_with_title_lbl.setPixmap(QPixmap(u":/icon/new-title-resize.png"))

        self.verticalLayout_9.addWidget(self.logo_with_title_lbl, 0, Qt.AlignLeft)

        self.frame = QFrame(self.SideMenuBar)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: transparent;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy1)
        self.frame1.setMinimumSize(QSize(178, 0))
        self.frame1.setStyleSheet(u"QFrame {background: rgba(46, 2, 102, 0.5);\n"
"border-radius: 25px;\n"
"};\n"
"\n"
"")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.a_2 = QWidget(self.frame1)
        self.a_2.setObjectName(u"a_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.a_2.sizePolicy().hasHeightForWidth())
        self.a_2.setSizePolicy(sizePolicy2)
        self.a_2.setStyleSheet(u"")
        self.horizontalLayout_28 = QHBoxLayout(self.a_2)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn_2 = QPushButton(self.a_2)
        self.dashboard_btn_2.setObjectName(u"dashboard_btn_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dashboard_btn_2.sizePolicy().hasHeightForWidth())
        self.dashboard_btn_2.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.dashboard_btn_2.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons8-dashboard-layout-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn_2.setIcon(icon1)
        self.dashboard_btn_2.setIconSize(QSize(30, 30))
        self.dashboard_btn_2.setFlat(True)

        self.horizontalLayout_28.addWidget(self.dashboard_btn_2)


        self.verticalLayout_8.addWidget(self.a_2)

        self.line_4 = QFrame(self.frame1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"border: 3px dotted white;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_4)

        self.d_2 = QWidget(self.frame1)
        self.d_2.setObjectName(u"d_2")
        sizePolicy2.setHeightForWidth(self.d_2.sizePolicy().hasHeightForWidth())
        self.d_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_31 = QHBoxLayout(self.d_2)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.parental_btn_2 = QPushButton(self.d_2)
        self.parental_btn_2.setObjectName(u"parental_btn_2")
        sizePolicy3.setHeightForWidth(self.parental_btn_2.sizePolicy().hasHeightForWidth())
        self.parental_btn_2.setSizePolicy(sizePolicy3)
        self.parental_btn_2.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons8-switches-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parental_btn_2.setIcon(icon2)
        self.parental_btn_2.setIconSize(QSize(25, 25))
        self.parental_btn_2.setFlat(True)

        self.horizontalLayout_31.addWidget(self.parental_btn_2)


        self.verticalLayout_8.addWidget(self.d_2)

        self.line_7 = QFrame(self.frame1)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"border: 3px dotted white;")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.c_2 = QWidget(self.frame1)
        self.c_2.setObjectName(u"c_2")
        sizePolicy2.setHeightForWidth(self.c_2.sizePolicy().hasHeightForWidth())
        self.c_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_33 = QHBoxLayout(self.c_2)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.settings_btn_2 = QPushButton(self.c_2)
        self.settings_btn_2.setObjectName(u"settings_btn_2")
        sizePolicy3.setHeightForWidth(self.settings_btn_2.sizePolicy().hasHeightForWidth())
        self.settings_btn_2.setSizePolicy(sizePolicy3)
        self.settings_btn_2.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons8-setting-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn_2.setIcon(icon3)
        self.settings_btn_2.setIconSize(QSize(25, 25))
        self.settings_btn_2.setFlat(True)

        self.horizontalLayout_33.addWidget(self.settings_btn_2)


        self.verticalLayout_8.addWidget(self.c_2)


        self.verticalLayout_11.addWidget(self.frame1)


        self.verticalLayout_9.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.SideMenuBar)

        self.MainContentFrame = QFrame(self.widget)
        self.MainContentFrame.setObjectName(u"MainContentFrame")
        self.MainContentFrame.setFrameShape(QFrame.StyledPanel)
        self.MainContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainContentFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WindowBar = QFrame(self.MainContentFrame)
        self.WindowBar.setObjectName(u"WindowBar")
        self.WindowBar.setFrameShape(QFrame.StyledPanel)
        self.WindowBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.WindowBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.ActionFrame = QFrame(self.WindowBar)
        self.ActionFrame.setObjectName(u"ActionFrame")
        self.ActionFrame.setStyleSheet(u"*{border:None;}")
        self.ActionFrame.setFrameShape(QFrame.StyledPanel)
        self.ActionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ActionFrame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.min_btn = QPushButton(self.ActionFrame)
        self.min_btn.setObjectName(u"min_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons8-minimize-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon4)
        self.min_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.min_btn)

        self.close_btn = QPushButton(self.ActionFrame)
        self.close_btn.setObjectName(u"close_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons8-close-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon5)
        self.close_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.close_btn)


        self.horizontalLayout_4.addWidget(self.ActionFrame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.WindowBar)

        self.cont_stackedwidget = QStackedWidget(self.MainContentFrame)
        self.cont_stackedwidget.setObjectName(u"cont_stackedwidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cont_stackedwidget.sizePolicy().hasHeightForWidth())
        self.cont_stackedwidget.setSizePolicy(sizePolicy4)
        self.cont_stackedwidget.setStyleSheet(u"background-color: transparent;")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.verticalLayout_19 = QVBoxLayout(self.Dashboard)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Frame = QFrame(self.Dashboard)
        self.Frame.setObjectName(u"Frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Frame.sizePolicy().hasHeightForWidth())
        self.Frame.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setKerning(True)
        self.Frame.setFont(font1)
        self.Frame.setFrameShape(QFrame.StyledPanel)
        self.Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.Frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.UseTimeFrame = QFrame(self.frame_2)
        self.UseTimeFrame.setObjectName(u"UseTimeFrame")
        self.UseTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.UseTimeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.UseTimeFrame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_8 = QFrame(self.UseTimeFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setKerning(True)
        self.label_3.setFont(font2)
        self.label_3.setPixmap(QPixmap(u":/icon/tut-title-resize.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_3)

        self.popout_btn = QPushButton(self.frame_8)
        self.popout_btn.setObjectName(u"popout_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons8-popup-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.popout_btn.setIcon(icon6)
        self.popout_btn.setIconSize(QSize(20, 20))
        self.popout_btn.setFlat(True)

        self.horizontalLayout_15.addWidget(self.popout_btn)


        self.verticalLayout_23.addWidget(self.frame_8)

        self.line_5 = QFrame(self.UseTimeFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background: white;")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_5)

        self.use_time_lbl = QLabel(self.UseTimeFrame)
        self.use_time_lbl.setObjectName(u"use_time_lbl")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        font3.setKerning(True)
        self.use_time_lbl.setFont(font3)
        self.use_time_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.use_time_lbl)


        self.horizontalLayout_18.addWidget(self.UseTimeFrame, 0, Qt.AlignRight)

        self.MonitorFrame = QFrame(self.frame_2)
        self.MonitorFrame.setObjectName(u"MonitorFrame")
        self.MonitorFrame.setFrameShape(QFrame.StyledPanel)
        self.MonitorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.MonitorFrame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.MonitorFrame)
        self.frame_11.setObjectName(u"frame_11")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        self.frame_11.setFont(font4)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.monitor_btn = QPushButton(self.frame_11)
        self.monitor_btn.setObjectName(u"monitor_btn")
        self.monitor_btn.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons8-startup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.monitor_btn.setIcon(icon7)
        self.monitor_btn.setIconSize(QSize(55, 55))

        self.verticalLayout_12.addWidget(self.monitor_btn)


        self.horizontalLayout_16.addWidget(self.frame_11)

        self.frame_3 = QFrame(self.MonitorFrame)
        self.frame_3.setObjectName(u"frame_3")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(20)
        self.frame_3.setFont(font5)
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"background-color: #5e00b0;\n"
"padding: 5px 20px 5px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #a200ff;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.refresh_chart_btn = QPushButton(self.frame_3)
        self.refresh_chart_btn.setObjectName(u"refresh_chart_btn")
        self.refresh_chart_btn.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.refresh_chart_btn)

        self.use_time_btn = QPushButton(self.frame_3)
        self.use_time_btn.setObjectName(u"use_time_btn")
        sizePolicy5.setHeightForWidth(self.use_time_btn.sizePolicy().hasHeightForWidth())
        self.use_time_btn.setSizePolicy(sizePolicy5)
        self.use_time_btn.setMinimumSize(QSize(125, 0))
        self.use_time_btn.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.use_time_btn, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.frame_3)


        self.horizontalLayout_18.addWidget(self.MonitorFrame, 0, Qt.AlignLeft)


        self.verticalLayout_22.addWidget(self.frame_2)

        self.chart_cont = QGridLayout()
        self.chart_cont.setObjectName(u"chart_cont")

        self.verticalLayout_22.addLayout(self.chart_cont)


        self.verticalLayout_19.addWidget(self.Frame)

        self.cont_stackedwidget.addWidget(self.Dashboard)
        self.ParentalControl = QWidget()
        self.ParentalControl.setObjectName(u"ParentalControl")
        self.verticalLayout_5 = QVBoxLayout(self.ParentalControl)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.UsetimeFame_2 = QFrame(self.ParentalControl)
        self.UsetimeFame_2.setObjectName(u"UsetimeFame_2")
        self.UsetimeFame_2.setFrameShape(QFrame.StyledPanel)
        self.UsetimeFame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.UsetimeFame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.frame_10 = QFrame(self.UsetimeFame_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.table_lbl = QLabel(self.frame_10)
        self.table_lbl.setObjectName(u"table_lbl")
        sizePolicy.setHeightForWidth(self.table_lbl.sizePolicy().hasHeightForWidth())
        self.table_lbl.setSizePolicy(sizePolicy)
        self.table_lbl.setPixmap(QPixmap(u":/icon/access-title-resize.png"))
        self.table_lbl.setScaledContents(False)

        self.horizontalLayout_14.addWidget(self.table_lbl)

        self.parental_setting_btn = QPushButton(self.frame_10)
        self.parental_setting_btn.setObjectName(u"parental_setting_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons8-control-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parental_setting_btn.setIcon(icon8)
        self.parental_setting_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.parental_setting_btn, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.UsetimeFame_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy6)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(1)
        self.frame_14.setFont(font6)
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(13)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        self.label_8.setFont(font7)

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.wed_box = QDoubleSpinBox(self.frame_14)
        self.wed_box.setObjectName(u"wed_box")

        self.gridLayout_2.addWidget(self.wed_box, 3, 1, 1, 1)

        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.mon_box = QDoubleSpinBox(self.frame_14)
        self.mon_box.setObjectName(u"mon_box")

        self.gridLayout_2.addWidget(self.mon_box, 1, 1, 1, 1)

        self.sat_box = QDoubleSpinBox(self.frame_14)
        self.sat_box.setObjectName(u"sat_box")

        self.gridLayout_2.addWidget(self.sat_box, 6, 1, 1, 1)

        self.sun_box = QDoubleSpinBox(self.frame_14)
        self.sun_box.setObjectName(u"sun_box")

        self.gridLayout_2.addWidget(self.sun_box, 7, 1, 1, 1)

        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.tue_box = QDoubleSpinBox(self.frame_14)
        self.tue_box.setObjectName(u"tue_box")

        self.gridLayout_2.addWidget(self.tue_box, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.fri_box = QDoubleSpinBox(self.frame_14)
        self.fri_box.setObjectName(u"fri_box")

        self.gridLayout_2.addWidget(self.fri_box, 5, 1, 1, 1)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.thu_box = QDoubleSpinBox(self.frame_14)
        self.thu_box.setObjectName(u"thu_box")

        self.gridLayout_2.addWidget(self.thu_box, 4, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_14)

        self.usetime_table = QTableWidget(self.frame_13)
        if (self.usetime_table.columnCount() < 24):
            self.usetime_table.setColumnCount(24)
        __qtablewidgetitem = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.usetime_table.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        if (self.usetime_table.rowCount() < 7):
            self.usetime_table.setRowCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.usetime_table.setVerticalHeaderItem(6, __qtablewidgetitem30)
        self.usetime_table.setObjectName(u"usetime_table")
        sizePolicy6.setHeightForWidth(self.usetime_table.sizePolicy().hasHeightForWidth())
        self.usetime_table.setSizePolicy(sizePolicy6)
        self.usetime_table.setStyleSheet(u"QTableWidget { border: none; gridline-color: #956a9e;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section ,QTableCornerButton::section{\n"
"    background-color: #9D43C9;\n"
"}")
        self.usetime_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.usetime_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.usetime_table.setShowGrid(True)
        self.usetime_table.setGridStyle(Qt.DashLine)
        self.usetime_table.horizontalHeader().setVisible(True)
        self.usetime_table.horizontalHeader().setMinimumSectionSize(30)
        self.usetime_table.horizontalHeader().setDefaultSectionSize(30)
        self.usetime_table.verticalHeader().setVisible(False)

        self.horizontalLayout_20.addWidget(self.usetime_table)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_5 = QFrame(self.UsetimeFame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.parental_box = QCheckBox(self.frame_5)
        self.parental_box.setObjectName(u"parental_box")
        self.parental_box.setFont(font)
        self.parental_box.setStyleSheet(u"QCheckBox {\n"
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
"")

        self.horizontalLayout_11.addWidget(self.parental_box, 0, Qt.AlignLeft)

        self.usetime_btn = QPushButton(self.frame_5)
        self.usetime_btn.setObjectName(u"usetime_btn")
        self.usetime_btn.setStyleSheet(u"QPushButton {background-color: #00d991;}\n"
"QPushButton:hover{background-color: #00fca8;}\n"
"QPushButton:pressed{background-color: #00fca8;}")

        self.horizontalLayout_11.addWidget(self.usetime_btn, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.UsetimeFame_2)

        self.cont_stackedwidget.addWidget(self.ParentalControl)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.verticalLayout_6 = QVBoxLayout(self.Settings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.SettingOptionFrame = QFrame(self.Settings)
        self.SettingOptionFrame.setObjectName(u"SettingOptionFrame")
        self.SettingOptionFrame.setMinimumSize(QSize(400, 400))
        self.SettingOptionFrame.setStyleSheet(u"\n"
"QComboBox {\n"
"    border-radius: 3px;\n"
"    min-width: 8em;\n"
"	background: #7346ad;\n"
"	padding: 3px\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:  #3b006e;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color:  #3b006e;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-image: url(:/icon/icons8-down-48.png) 4;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.verticalLayout_26 = QVBoxLayout(self.SettingOptionFrame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.OptionFrame = QFrame(self.SettingOptionFrame)
        self.OptionFrame.setObjectName(u"OptionFrame")
        sizePolicy.setHeightForWidth(self.OptionFrame.sizePolicy().hasHeightForWidth())
        self.OptionFrame.setSizePolicy(sizePolicy)
        self.OptionFrame.setFrameShape(QFrame.StyledPanel)
        self.OptionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.OptionFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(20, 0, 0, 0)
        self.start_box = QCheckBox(self.OptionFrame)
        self.start_box.setObjectName(u"start_box")
        sizePolicy6.setHeightForWidth(self.start_box.sizePolicy().hasHeightForWidth())
        self.start_box.setSizePolicy(sizePolicy6)
        self.start_box.setFont(font)

        self.horizontalLayout_27.addWidget(self.start_box)

        self.background_box = QCheckBox(self.OptionFrame)
        self.background_box.setObjectName(u"background_box")
        sizePolicy6.setHeightForWidth(self.background_box.sizePolicy().hasHeightForWidth())
        self.background_box.setSizePolicy(sizePolicy6)
        self.background_box.setFont(font)

        self.horizontalLayout_27.addWidget(self.background_box)


        self.verticalLayout_26.addWidget(self.OptionFrame)

        self.frame_4 = QFrame(self.SettingOptionFrame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.app_time_track_box = QCheckBox(self.frame_4)
        self.app_time_track_box.setObjectName(u"app_time_track_box")
        sizePolicy6.setHeightForWidth(self.app_time_track_box.sizePolicy().hasHeightForWidth())
        self.app_time_track_box.setSizePolicy(sizePolicy6)
        self.app_time_track_box.setFont(font)

        self.horizontalLayout_10.addWidget(self.app_time_track_box)

        self.theme_box = QCheckBox(self.frame_4)
        self.theme_box.setObjectName(u"theme_box")
        sizePolicy6.setHeightForWidth(self.theme_box.sizePolicy().hasHeightForWidth())
        self.theme_box.setSizePolicy(sizePolicy6)
        self.theme_box.setFont(font)

        self.horizontalLayout_10.addWidget(self.theme_box)


        self.verticalLayout_26.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.BreakFrame = QFrame(self.SettingOptionFrame)
        self.BreakFrame.setObjectName(u"BreakFrame")
        sizePolicy.setHeightForWidth(self.BreakFrame.sizePolicy().hasHeightForWidth())
        self.BreakFrame.setSizePolicy(sizePolicy)
        self.BreakFrame.setFrameShape(QFrame.StyledPanel)
        self.BreakFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.BreakFrame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.BreakFrame)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy7)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.reminder_lbl = QLabel(self.frame_36)
        self.reminder_lbl.setObjectName(u"reminder_lbl")
        sizePolicy7.setHeightForWidth(self.reminder_lbl.sizePolicy().hasHeightForWidth())
        self.reminder_lbl.setSizePolicy(sizePolicy7)
        self.reminder_lbl.setFont(font)

        self.horizontalLayout_23.addWidget(self.reminder_lbl)

        self.reminder_box = QDoubleSpinBox(self.frame_36)
        self.reminder_box.setObjectName(u"reminder_box")
        self.reminder_box.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.reminder_box)


        self.horizontalLayout_22.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.BreakFrame)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy7.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy7)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.notify_box = QCheckBox(self.frame_37)
        self.notify_box.setObjectName(u"notify_box")
        sizePolicy5.setHeightForWidth(self.notify_box.sizePolicy().hasHeightForWidth())
        self.notify_box.setSizePolicy(sizePolicy5)
        self.notify_box.setFont(font)

        self.verticalLayout_27.addWidget(self.notify_box)


        self.horizontalLayout_22.addWidget(self.frame_37)


        self.verticalLayout_26.addWidget(self.BreakFrame)

        self.AlertFrame = QFrame(self.SettingOptionFrame)
        self.AlertFrame.setObjectName(u"AlertFrame")
        sizePolicy.setHeightForWidth(self.AlertFrame.sizePolicy().hasHeightForWidth())
        self.AlertFrame.setSizePolicy(sizePolicy)
        self.AlertFrame.setFrameShape(QFrame.StyledPanel)
        self.AlertFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.AlertFrame)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.alert_lbl = QLabel(self.AlertFrame)
        self.alert_lbl.setObjectName(u"alert_lbl")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.alert_lbl.sizePolicy().hasHeightForWidth())
        self.alert_lbl.setSizePolicy(sizePolicy8)
        self.alert_lbl.setBaseSize(QSize(1, 0))
        self.alert_lbl.setFont(font)
        self.alert_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.alert_lbl, 0, Qt.AlignRight)

        self.alert_box = QComboBox(self.AlertFrame)
        self.alert_box.addItem("")
        self.alert_box.addItem("")
        self.alert_box.setObjectName(u"alert_box")
        sizePolicy6.setHeightForWidth(self.alert_box.sizePolicy().hasHeightForWidth())
        self.alert_box.setSizePolicy(sizePolicy6)
        self.alert_box.setMinimumSize(QSize(118, 0))
        self.alert_box.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.alert_box, 0, Qt.AlignLeft)


        self.verticalLayout_26.addWidget(self.AlertFrame)

        self.CameraFrame = QFrame(self.SettingOptionFrame)
        self.CameraFrame.setObjectName(u"CameraFrame")
        sizePolicy.setHeightForWidth(self.CameraFrame.sizePolicy().hasHeightForWidth())
        self.CameraFrame.setSizePolicy(sizePolicy)
        self.CameraFrame.setFrameShape(QFrame.StyledPanel)
        self.CameraFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.CameraFrame)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.camera_lbl = QLabel(self.CameraFrame)
        self.camera_lbl.setObjectName(u"camera_lbl")
        self.camera_lbl.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.camera_lbl.sizePolicy().hasHeightForWidth())
        self.camera_lbl.setSizePolicy(sizePolicy8)
        self.camera_lbl.setFont(font)
        self.camera_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.camera_lbl, 0, Qt.AlignRight)

        self.camera_box = QComboBox(self.CameraFrame)
        self.camera_box.setObjectName(u"camera_box")
        sizePolicy6.setHeightForWidth(self.camera_box.sizePolicy().hasHeightForWidth())
        self.camera_box.setSizePolicy(sizePolicy6)
        self.camera_box.setMinimumSize(QSize(118, 0))

        self.horizontalLayout_25.addWidget(self.camera_box, 0, Qt.AlignLeft)


        self.verticalLayout_26.addWidget(self.CameraFrame)

        self.SettingsBtnFrame = QFrame(self.SettingOptionFrame)
        self.SettingsBtnFrame.setObjectName(u"SettingsBtnFrame")
        sizePolicy.setHeightForWidth(self.SettingsBtnFrame.sizePolicy().hasHeightForWidth())
        self.SettingsBtnFrame.setSizePolicy(sizePolicy)
        self.SettingsBtnFrame.setStyleSheet(u"QPushButton{\n"
"background-color: #3b006e;\n"
"padding: 5px 20px 5px 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #a200ff;\n"
"}\n"
"\n"
"QPushButton#apply_btn{\n"
"background-color: #02a36e;\n"
"}\n"
"\n"
"QPushButton#apply_btn:hover{\n"
"background: #00fca8;\n"
"}\n"
"\n"
"QPushButton#remove_data_btn{\n"
"background-color: #a10000;\n"
"}\n"
"\n"
"QPushButton#remove_data_btn:hover{\n"
"background: #d10000;\n"
"}\n"
"\n"
"")
        self.SettingsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.SettingsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.SettingsBtnFrame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.reset_btn = QPushButton(self.SettingsBtnFrame)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_26.addWidget(self.reset_btn)

        self.remove_data_btn = QPushButton(self.SettingsBtnFrame)
        self.remove_data_btn.setObjectName(u"remove_data_btn")
        self.remove_data_btn.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.remove_data_btn)

        self.apply_btn = QPushButton(self.SettingsBtnFrame)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.apply_btn)


        self.verticalLayout_26.addWidget(self.SettingsBtnFrame)

        self.frame_7 = QFrame(self.SettingOptionFrame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.web_btn = QPushButton(self.frame_7)
        self.web_btn.setObjectName(u"web_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons8-info-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.web_btn.setIcon(icon9)
        self.web_btn.setFlat(True)

        self.horizontalLayout_12.addWidget(self.web_btn)

        self.update_btn = QPushButton(self.frame_7)
        self.update_btn.setObjectName(u"update_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons8-question-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_btn.setIcon(icon10)
        self.update_btn.setFlat(True)

        self.horizontalLayout_12.addWidget(self.update_btn)


        self.verticalLayout_26.addWidget(self.frame_7)

        self.app_ver_label = QLabel(self.SettingOptionFrame)
        self.app_ver_label.setObjectName(u"app_ver_label")
        sizePolicy.setHeightForWidth(self.app_ver_label.sizePolicy().hasHeightForWidth())
        self.app_ver_label.setSizePolicy(sizePolicy)

        self.verticalLayout_26.addWidget(self.app_ver_label, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.SettingOptionFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cont_stackedwidget.addWidget(self.Settings)
        self.Authenticate = QWidget()
        self.Authenticate.setObjectName(u"Authenticate")
        self.horizontalLayout_8 = QHBoxLayout(self.Authenticate)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.PIN_stackedwidget = QStackedWidget(self.Authenticate)
        self.PIN_stackedwidget.setObjectName(u"PIN_stackedwidget")
        self.ChangePINPage = QWidget()
        self.ChangePINPage.setObjectName(u"ChangePINPage")
        self.verticalLayout = QVBoxLayout(self.ChangePINPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.page_hint_lbl = QLabel(self.ChangePINPage)
        self.page_hint_lbl.setObjectName(u"page_hint_lbl")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.page_hint_lbl.sizePolicy().hasHeightForWidth())
        self.page_hint_lbl.setSizePolicy(sizePolicy9)
        self.page_hint_lbl.setFont(font)
        self.page_hint_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.page_hint_lbl, 0, Qt.AlignLeft)

        self.UsernameFrame = QFrame(self.ChangePINPage)
        self.UsernameFrame.setObjectName(u"UsernameFrame")
        self.UsernameFrame.setFrameShape(QFrame.StyledPanel)
        self.UsernameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.UsernameFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.username_lbl = QLabel(self.UsernameFrame)
        self.username_lbl.setObjectName(u"username_lbl")

        self.horizontalLayout_19.addWidget(self.username_lbl)

        self.username_line = QLineEdit(self.UsernameFrame)
        self.username_line.setObjectName(u"username_line")
        sizePolicy5.setHeightForWidth(self.username_line.sizePolicy().hasHeightForWidth())
        self.username_line.setSizePolicy(sizePolicy5)

        self.horizontalLayout_19.addWidget(self.username_line)


        self.verticalLayout.addWidget(self.UsernameFrame)

        self.OldPINFrame = QFrame(self.ChangePINPage)
        self.OldPINFrame.setObjectName(u"OldPINFrame")
        sizePolicy.setHeightForWidth(self.OldPINFrame.sizePolicy().hasHeightForWidth())
        self.OldPINFrame.setSizePolicy(sizePolicy)
        self.OldPINFrame.setFrameShape(QFrame.StyledPanel)
        self.OldPINFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.OldPINFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.old_PIN_lbl = QLabel(self.OldPINFrame)
        self.old_PIN_lbl.setObjectName(u"old_PIN_lbl")

        self.horizontalLayout_5.addWidget(self.old_PIN_lbl)

        self.old_PIN_line = QLineEdit(self.OldPINFrame)
        self.old_PIN_line.setObjectName(u"old_PIN_line")
        sizePolicy5.setHeightForWidth(self.old_PIN_line.sizePolicy().hasHeightForWidth())
        self.old_PIN_line.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.old_PIN_line)


        self.verticalLayout.addWidget(self.OldPINFrame)

        self.NewPINFrame = QFrame(self.ChangePINPage)
        self.NewPINFrame.setObjectName(u"NewPINFrame")
        sizePolicy.setHeightForWidth(self.NewPINFrame.sizePolicy().hasHeightForWidth())
        self.NewPINFrame.setSizePolicy(sizePolicy)
        self.NewPINFrame.setFrameShape(QFrame.StyledPanel)
        self.NewPINFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.NewPINFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.new_PIN_lbl = QLabel(self.NewPINFrame)
        self.new_PIN_lbl.setObjectName(u"new_PIN_lbl")

        self.horizontalLayout_3.addWidget(self.new_PIN_lbl)

        self.new_PIN_line = QLineEdit(self.NewPINFrame)
        self.new_PIN_line.setObjectName(u"new_PIN_line")
        sizePolicy5.setHeightForWidth(self.new_PIN_line.sizePolicy().hasHeightForWidth())
        self.new_PIN_line.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.new_PIN_line)


        self.verticalLayout.addWidget(self.NewPINFrame)

        self.ConfirmPINFrame = QFrame(self.ChangePINPage)
        self.ConfirmPINFrame.setObjectName(u"ConfirmPINFrame")
        sizePolicy.setHeightForWidth(self.ConfirmPINFrame.sizePolicy().hasHeightForWidth())
        self.ConfirmPINFrame.setSizePolicy(sizePolicy)
        self.ConfirmPINFrame.setFrameShape(QFrame.StyledPanel)
        self.ConfirmPINFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ConfirmPINFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.confirm_lbl = QLabel(self.ConfirmPINFrame)
        self.confirm_lbl.setObjectName(u"confirm_lbl")

        self.horizontalLayout_6.addWidget(self.confirm_lbl)

        self.confirm_PIN_line = QLineEdit(self.ConfirmPINFrame)
        self.confirm_PIN_line.setObjectName(u"confirm_PIN_line")
        sizePolicy5.setHeightForWidth(self.confirm_PIN_line.sizePolicy().hasHeightForWidth())
        self.confirm_PIN_line.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.confirm_PIN_line)


        self.verticalLayout.addWidget(self.ConfirmPINFrame)

        self.change_PIN_hint_lbl = QLabel(self.ChangePINPage)
        self.change_PIN_hint_lbl.setObjectName(u"change_PIN_hint_lbl")
        sizePolicy9.setHeightForWidth(self.change_PIN_hint_lbl.sizePolicy().hasHeightForWidth())
        self.change_PIN_hint_lbl.setSizePolicy(sizePolicy9)
        self.change_PIN_hint_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.change_PIN_hint_lbl, 0, Qt.AlignHCenter)

        self.change_PIN_btn = QPushButton(self.ChangePINPage)
        self.change_PIN_btn.setObjectName(u"change_PIN_btn")
        sizePolicy6.setHeightForWidth(self.change_PIN_btn.sizePolicy().hasHeightForWidth())
        self.change_PIN_btn.setSizePolicy(sizePolicy6)
        self.change_PIN_btn.setStyleSheet(u"QPushButton{\n"
"padding: 3px 25px 3px 25px;\n"
"background-color: #00d991;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #00fca8;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.change_PIN_btn, 0, Qt.AlignHCenter)

        self.PIN_stackedwidget.addWidget(self.ChangePINPage)
        self.PINValidationPage = QWidget()
        self.PINValidationPage.setObjectName(u"PINValidationPage")
        self.verticalLayout_3 = QVBoxLayout(self.PINValidationPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PINValidationFrame = QFrame(self.PINValidationPage)
        self.PINValidationFrame.setObjectName(u"PINValidationFrame")
        self.PINValidationFrame.setFrameShape(QFrame.StyledPanel)
        self.PINValidationFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.PINValidationFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.PINValidationFrame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.PINFrame = QFrame(self.PINValidationFrame)
        self.PINFrame.setObjectName(u"PINFrame")
        self.PINFrame.setFrameShape(QFrame.StyledPanel)
        self.PINFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.PINFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.PIN_line = QLineEdit(self.PINFrame)
        self.PIN_line.setObjectName(u"PIN_line")

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

        self.PIN_checkbox = QCheckBox(self.PINValidationFrame)
        self.PIN_checkbox.setObjectName(u"PIN_checkbox")
        self.PIN_checkbox.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/icons8-unchecked-radio-button-48.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/icons8-checked-radio-button-48.png);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}")

        self.verticalLayout_4.addWidget(self.PIN_checkbox)

        self.PIN_hint_lbl = QLabel(self.PINValidationFrame)
        self.PIN_hint_lbl.setObjectName(u"PIN_hint_lbl")
        sizePolicy.setHeightForWidth(self.PIN_hint_lbl.sizePolicy().hasHeightForWidth())
        self.PIN_hint_lbl.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.PIN_hint_lbl, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.PINValidationFrame, 0, Qt.AlignVCenter)

        self.PIN_stackedwidget.addWidget(self.PINValidationPage)

        self.horizontalLayout_8.addWidget(self.PIN_stackedwidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cont_stackedwidget.addWidget(self.Authenticate)

        self.verticalLayout_2.addWidget(self.cont_stackedwidget)


        self.horizontalLayout_2.addWidget(self.MainContentFrame)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        self.cont_stackedwidget.setCurrentIndex(2)
        self.PIN_stackedwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Align Position", None))
        self.logo_with_title_lbl.setText("")
        self.dashboard_btn_2.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.parental_btn_2.setText(QCoreApplication.translate("MainWindow", u"  Parental\n"
"  Control", None))
        self.settings_btn_2.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.min_btn.setText("")
        self.close_btn.setText("")
        self.label_3.setText("")
        self.popout_btn.setText("")
        self.use_time_lbl.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.monitor_btn.setText("")
        self.refresh_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.use_time_btn.setText(QCoreApplication.translate("MainWindow", u"Use Time", None))
        self.table_lbl.setText("")
        self.parental_setting_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sat", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sun", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fri", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mon", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Thu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Wed", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time Limit", None))
        ___qtablewidgetitem = self.usetime_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.usetime_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.usetime_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.usetime_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.usetime_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem5 = self.usetime_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem6 = self.usetime_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem7 = self.usetime_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem8 = self.usetime_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem9 = self.usetime_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem10 = self.usetime_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem11 = self.usetime_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem12 = self.usetime_table.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem13 = self.usetime_table.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem14 = self.usetime_table.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem15 = self.usetime_table.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem16 = self.usetime_table.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem17 = self.usetime_table.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem18 = self.usetime_table.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem19 = self.usetime_table.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem20 = self.usetime_table.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem21 = self.usetime_table.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem22 = self.usetime_table.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem23 = self.usetime_table.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem24 = self.usetime_table.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Mon", None));
        ___qtablewidgetitem25 = self.usetime_table.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Tue", None));
        ___qtablewidgetitem26 = self.usetime_table.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Wed", None));
        ___qtablewidgetitem27 = self.usetime_table.verticalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Thu", None));
        ___qtablewidgetitem28 = self.usetime_table.verticalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Fri", None));
        ___qtablewidgetitem29 = self.usetime_table.verticalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Sat", None));
        ___qtablewidgetitem30 = self.usetime_table.verticalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Sun", None));
        self.parental_box.setText(QCoreApplication.translate("MainWindow", u"Parental Option", None))
        self.usetime_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.start_box.setText(QCoreApplication.translate("MainWindow", u"Auto Start", None))
        self.background_box.setText(QCoreApplication.translate("MainWindow", u"Run In Background", None))
        self.app_time_track_box.setText(QCoreApplication.translate("MainWindow", u" App Use Time Tracking", None))
        self.theme_box.setText(QCoreApplication.translate("MainWindow", u" Light Theme", None))
        self.reminder_lbl.setText(QCoreApplication.translate("MainWindow", u"Break Time (mins)", None))
        self.notify_box.setText(QCoreApplication.translate("MainWindow", u"Break Reminder", None))
        self.alert_lbl.setText(QCoreApplication.translate("MainWindow", u"Alert Position", None))
        self.alert_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Left", None))
        self.alert_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Right", None))

        self.camera_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset Config", None))
        self.remove_data_btn.setText(QCoreApplication.translate("MainWindow", u"Reset All", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.web_btn.setText(QCoreApplication.translate("MainWindow", u"Info/Help", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"  Check Update", None))
        self.app_ver_label.setText(QCoreApplication.translate("MainWindow", u"App Version", None))
        self.page_hint_lbl.setText(QCoreApplication.translate("MainWindow", u"Create New PIN", None))
        self.username_lbl.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.old_PIN_lbl.setText(QCoreApplication.translate("MainWindow", u"Old PIN       ", None))
        self.new_PIN_lbl.setText(QCoreApplication.translate("MainWindow", u"New PIN     ", None))
        self.confirm_lbl.setText(QCoreApplication.translate("MainWindow", u"Confirm PIN", None))
        self.change_PIN_hint_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.change_PIN_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter your 6-digit PIN", None))
        self.PIN_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.PIN_checkbox.setText(QCoreApplication.translate("MainWindow", u"Remember me", None))
        self.PIN_hint_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

