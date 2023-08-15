# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import Window.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 512)
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 28, 48);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
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
        self.verticalLayout_9.setContentsMargins(-1, 0, 6, 0)
        self.logo_with_title_lbl = QLabel(self.SideMenuBar)
        self.logo_with_title_lbl.setObjectName(u"logo_with_title_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_with_title_lbl.sizePolicy().hasHeightForWidth())
        self.logo_with_title_lbl.setSizePolicy(sizePolicy)
        self.logo_with_title_lbl.setPixmap(QPixmap(u":/icon/little_logo.png"))
        self.logo_with_title_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.logo_with_title_lbl)

        self.frame_4 = QFrame(self.SideMenuBar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.dashboard_btn = QPushButton(self.frame_4)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons8-dashboard-layout-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon1)
        self.dashboard_btn.setIconSize(QSize(25, 25))
        self.dashboard_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.dashboard_btn, 0, Qt.AlignLeft)

        self.parental_btn = QPushButton(self.frame_4)
        self.parental_btn.setObjectName(u"parental_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons8-switches-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parental_btn.setIcon(icon2)
        self.parental_btn.setIconSize(QSize(25, 25))
        self.parental_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.parental_btn, 0, Qt.AlignLeft)

        self.calibrate_btn = QPushButton(self.frame_4)
        self.calibrate_btn.setObjectName(u"calibrate_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons8-tasks-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calibrate_btn.setIcon(icon3)
        self.calibrate_btn.setIconSize(QSize(25, 25))
        self.calibrate_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.calibrate_btn, 0, Qt.AlignLeft)

        self.settings_btn = QPushButton(self.frame_4)
        self.settings_btn.setObjectName(u"settings_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons8-setting-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QSize(25, 25))
        self.settings_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.settings_btn, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_4)


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
        self.frame_5 = QFrame(self.WindowBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.page_title_lbl = QLabel(self.WindowBar)
        self.page_title_lbl.setObjectName(u"page_title_lbl")
        font = QFont()
        font.setPointSize(12)
        self.page_title_lbl.setFont(font)

        self.horizontalLayout_4.addWidget(self.page_title_lbl, 0, Qt.AlignHCenter)

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
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons8-minimize-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon5)
        self.min_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.min_btn)

        self.close_btn = QPushButton(self.ActionFrame)
        self.close_btn.setObjectName(u"close_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons8-close-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon6)
        self.close_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.close_btn)


        self.horizontalLayout_4.addWidget(self.ActionFrame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.WindowBar)

        self.cont_stackedwidget = QStackedWidget(self.MainContentFrame)
        self.cont_stackedwidget.setObjectName(u"cont_stackedwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cont_stackedwidget.sizePolicy().hasHeightForWidth())
        self.cont_stackedwidget.setSizePolicy(sizePolicy1)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.verticalLayout_19 = QVBoxLayout(self.Dashboard)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Frame = QFrame(self.Dashboard)
        self.Frame.setObjectName(u"Frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Frame.sizePolicy().hasHeightForWidth())
        self.Frame.setSizePolicy(sizePolicy2)
        font1 = QFont()
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
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_3 = QLabel(self.UseTimeFrame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setKerning(True)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_3)

        self.use_time_lbl = QLabel(self.UseTimeFrame)
        self.use_time_lbl.setObjectName(u"use_time_lbl")
        self.use_time_lbl.setFont(font2)
        self.use_time_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.use_time_lbl)


        self.horizontalLayout_18.addWidget(self.UseTimeFrame, 0, Qt.AlignRight)

        self.MonitorFrame = QFrame(self.frame_2)
        self.MonitorFrame.setObjectName(u"MonitorFrame")
        self.MonitorFrame.setFrameShape(QFrame.StyledPanel)
        self.MonitorFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.MonitorFrame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.MonitorFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_16)

        self.popout_btn = QPushButton(self.frame)
        self.popout_btn.setObjectName(u"popout_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons8-popup-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.popout_btn.setIcon(icon7)
        self.popout_btn.setFlat(True)

        self.horizontalLayout_28.addWidget(self.popout_btn, 0, Qt.AlignRight)


        self.verticalLayout_24.addWidget(self.frame)

        self.line_4 = QFrame(self.MonitorFrame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(120, 0))
        self.line_4.setStyleSheet(u"background-color: rgb(218, 255, 251);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_4)

        self.monitor_btn = QPushButton(self.MonitorFrame)
        self.monitor_btn.setObjectName(u"monitor_btn")
        self.monitor_btn.setFont(font2)
        self.monitor_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

        self.verticalLayout_24.addWidget(self.monitor_btn)


        self.horizontalLayout_18.addWidget(self.MonitorFrame, 0, Qt.AlignLeft)


        self.verticalLayout_22.addWidget(self.frame_2)

        self.chart_cont = QGridLayout()
        self.chart_cont.setObjectName(u"chart_cont")

        self.verticalLayout_22.addLayout(self.chart_cont)

        self.frame_3 = QFrame(self.Frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.use_time_btn = QPushButton(self.frame_3)
        self.use_time_btn.setObjectName(u"use_time_btn")
        self.use_time_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")
        self.use_time_btn.setFlat(False)

        self.horizontalLayout_9.addWidget(self.use_time_btn, 0, Qt.AlignHCenter)

        self.refresh_chart_btn = QPushButton(self.frame_3)
        self.refresh_chart_btn.setObjectName(u"refresh_chart_btn")
        self.refresh_chart_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_9.addWidget(self.refresh_chart_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_3)


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
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.table_lbl = QLabel(self.UsetimeFame_2)
        self.table_lbl.setObjectName(u"table_lbl")

        self.verticalLayout_10.addWidget(self.table_lbl)

        self.usetime_table = QTableWidget(self.UsetimeFame_2)
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
        self.usetime_table.setMinimumSize(QSize(803, 234))
        self.usetime_table.setStyleSheet(u"QTableWidget { background-color: transparent; color: white;}\n"
"QTableWidget QHeaderView::section { background-color: rgb(23, 107, 135); color: white;}\n"
"QTableWidget QTableCornerButton::section {background-color: rgb(23, 107, 135) }\n"
"QTableWidget { border: none; }")
        self.usetime_table.setLineWidth(0)
        self.usetime_table.setCornerButtonEnabled(False)
        self.usetime_table.horizontalHeader().setDefaultSectionSize(32)

        self.verticalLayout_10.addWidget(self.usetime_table, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.TotalUsetimeFame = QFrame(self.UsetimeFame_2)
        self.TotalUsetimeFame.setObjectName(u"TotalUsetimeFame")
        self.TotalUsetimeFame.setFrameShape(QFrame.StyledPanel)
        self.TotalUsetimeFame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.TotalUsetimeFame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_6 = QFrame(self.TotalUsetimeFame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.usetime_lbl = QLabel(self.frame_6)
        self.usetime_lbl.setObjectName(u"usetime_lbl")

        self.horizontalLayout_12.addWidget(self.usetime_lbl)

        self.usetime_box = QDoubleSpinBox(self.frame_6)
        self.usetime_box.setObjectName(u"usetime_box")

        self.horizontalLayout_12.addWidget(self.usetime_box)


        self.horizontalLayout_10.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.parental_box = QCheckBox(self.TotalUsetimeFame)
        self.parental_box.setObjectName(u"parental_box")

        self.horizontalLayout_10.addWidget(self.parental_box, 0, Qt.AlignHCenter)

        self.usetime_btn = QPushButton(self.TotalUsetimeFame)
        self.usetime_btn.setObjectName(u"usetime_btn")
        self.usetime_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

        self.horizontalLayout_10.addWidget(self.usetime_btn, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.TotalUsetimeFame)


        self.verticalLayout_5.addWidget(self.UsetimeFame_2)

        self.OtherFrame = QFrame(self.ParentalControl)
        self.OtherFrame.setObjectName(u"OtherFrame")
        self.OtherFrame.setFrameShape(QFrame.StyledPanel)
        self.OtherFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.OtherFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.other_lbl = QLabel(self.OtherFrame)
        self.other_lbl.setObjectName(u"other_lbl")

        self.verticalLayout_13.addWidget(self.other_lbl, 0, Qt.AlignHCenter)

        self.ButtonFrame_2 = QFrame(self.OtherFrame)
        self.ButtonFrame_2.setObjectName(u"ButtonFrame_2")
        self.ButtonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.ButtonFrame_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.DataFrame = QFrame(self.ButtonFrame_2)
        self.DataFrame.setObjectName(u"DataFrame")
        self.DataFrame.setFrameShape(QFrame.StyledPanel)
        self.DataFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.DataFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.exct_data_btn = QPushButton(self.DataFrame)
        self.exct_data_btn.setObjectName(u"exct_data_btn")
        self.exct_data_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_11.addWidget(self.exct_data_btn, 0, Qt.AlignRight)

        self.restore_btn = QPushButton(self.DataFrame)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setEnabled(True)
        self.restore_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_11.addWidget(self.restore_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addWidget(self.DataFrame)

        self.changePIN_btn = QPushButton(self.ButtonFrame_2)
        self.changePIN_btn.setObjectName(u"changePIN_btn")
        self.changePIN_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_14.addWidget(self.changePIN_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.ButtonFrame_2)


        self.verticalLayout_5.addWidget(self.OtherFrame)

        self.cont_stackedwidget.addWidget(self.ParentalControl)
        self.Calibration = QWidget()
        self.Calibration.setObjectName(u"Calibration")
        self.verticalLayout_30 = QVBoxLayout(self.Calibration)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.calibrate_preview_lbl = QLabel(self.Calibration)
        self.calibrate_preview_lbl.setObjectName(u"calibrate_preview_lbl")

        self.verticalLayout_30.addWidget(self.calibrate_preview_lbl, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.CalibrateCameraFrame = QFrame(self.Calibration)
        self.CalibrateCameraFrame.setObjectName(u"CalibrateCameraFrame")
        self.CalibrateCameraFrame.setFrameShape(QFrame.StyledPanel)
        self.CalibrateCameraFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.CalibrateCameraFrame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.calibrate_camera_lbl = QLabel(self.CalibrateCameraFrame)
        self.calibrate_camera_lbl.setObjectName(u"calibrate_camera_lbl")
        self.calibrate_camera_lbl.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.calibrate_camera_lbl.sizePolicy().hasHeightForWidth())
        self.calibrate_camera_lbl.setSizePolicy(sizePolicy3)
        self.calibrate_camera_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.calibrate_camera_lbl)

        self.calibrate_camera_box = QComboBox(self.CalibrateCameraFrame)
        self.calibrate_camera_box.setObjectName(u"calibrate_camera_box")
        sizePolicy.setHeightForWidth(self.calibrate_camera_box.sizePolicy().hasHeightForWidth())
        self.calibrate_camera_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_30.addWidget(self.calibrate_camera_box)


        self.verticalLayout_30.addWidget(self.CalibrateCameraFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.hint_lbl = QLabel(self.Calibration)
        self.hint_lbl.setObjectName(u"hint_lbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hint_lbl.sizePolicy().hasHeightForWidth())
        self.hint_lbl.setSizePolicy(sizePolicy4)

        self.verticalLayout_30.addWidget(self.hint_lbl, 0, Qt.AlignHCenter)

        self.ButtonFrame = QFrame(self.Calibration)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.ButtonFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.recalibrate_btn = QPushButton(self.ButtonFrame)
        self.recalibrate_btn.setObjectName(u"recalibrate_btn")
        self.recalibrate_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

        self.horizontalLayout_29.addWidget(self.recalibrate_btn)

        self.proceed_btn = QPushButton(self.ButtonFrame)
        self.proceed_btn.setObjectName(u"proceed_btn")
        self.proceed_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

        self.horizontalLayout_29.addWidget(self.proceed_btn)

        self.append_btn = QPushButton(self.ButtonFrame)
        self.append_btn.setObjectName(u"append_btn")
        self.append_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_29.addWidget(self.append_btn)

        self.cancel_btn = QPushButton(self.ButtonFrame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_29.addWidget(self.cancel_btn)


        self.verticalLayout_30.addWidget(self.ButtonFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cont_stackedwidget.addWidget(self.Calibration)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.verticalLayout_6 = QVBoxLayout(self.Settings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.SettingOptionFrame = QFrame(self.Settings)
        self.SettingOptionFrame.setObjectName(u"SettingOptionFrame")
        self.SettingOptionFrame.setMinimumSize(QSize(400, 400))
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
        sizePolicy4.setHeightForWidth(self.start_box.sizePolicy().hasHeightForWidth())
        self.start_box.setSizePolicy(sizePolicy4)

        self.horizontalLayout_27.addWidget(self.start_box)

        self.background_box = QCheckBox(self.OptionFrame)
        self.background_box.setObjectName(u"background_box")
        sizePolicy4.setHeightForWidth(self.background_box.sizePolicy().hasHeightForWidth())
        self.background_box.setSizePolicy(sizePolicy4)

        self.horizontalLayout_27.addWidget(self.background_box)

        self.app_time_track_box = QCheckBox(self.OptionFrame)
        self.app_time_track_box.setObjectName(u"app_time_track_box")

        self.horizontalLayout_27.addWidget(self.app_time_track_box)


        self.verticalLayout_26.addWidget(self.OptionFrame)

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy5)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.reminder_lbl = QLabel(self.frame_36)
        self.reminder_lbl.setObjectName(u"reminder_lbl")
        sizePolicy5.setHeightForWidth(self.reminder_lbl.sizePolicy().hasHeightForWidth())
        self.reminder_lbl.setSizePolicy(sizePolicy5)

        self.horizontalLayout_23.addWidget(self.reminder_lbl)

        self.reminder_box = QDoubleSpinBox(self.frame_36)
        self.reminder_box.setObjectName(u"reminder_box")

        self.horizontalLayout_23.addWidget(self.reminder_box)


        self.horizontalLayout_22.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.BreakFrame)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy5.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy5)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.notify_box = QCheckBox(self.frame_37)
        self.notify_box.setObjectName(u"notify_box")
        sizePolicy2.setHeightForWidth(self.notify_box.sizePolicy().hasHeightForWidth())
        self.notify_box.setSizePolicy(sizePolicy2)

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
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.alert_lbl = QLabel(self.AlertFrame)
        self.alert_lbl.setObjectName(u"alert_lbl")
        sizePolicy3.setHeightForWidth(self.alert_lbl.sizePolicy().hasHeightForWidth())
        self.alert_lbl.setSizePolicy(sizePolicy3)
        self.alert_lbl.setBaseSize(QSize(1, 0))
        self.alert_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.alert_lbl)

        self.alert_box = QComboBox(self.AlertFrame)
        self.alert_box.addItem("")
        self.alert_box.addItem("")
        self.alert_box.setObjectName(u"alert_box")
        sizePolicy.setHeightForWidth(self.alert_box.sizePolicy().hasHeightForWidth())
        self.alert_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_24.addWidget(self.alert_box)


        self.verticalLayout_26.addWidget(self.AlertFrame)

        self.CameraFrame = QFrame(self.SettingOptionFrame)
        self.CameraFrame.setObjectName(u"CameraFrame")
        sizePolicy.setHeightForWidth(self.CameraFrame.sizePolicy().hasHeightForWidth())
        self.CameraFrame.setSizePolicy(sizePolicy)
        self.CameraFrame.setFrameShape(QFrame.StyledPanel)
        self.CameraFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.CameraFrame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.camera_lbl = QLabel(self.CameraFrame)
        self.camera_lbl.setObjectName(u"camera_lbl")
        self.camera_lbl.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.camera_lbl.sizePolicy().hasHeightForWidth())
        self.camera_lbl.setSizePolicy(sizePolicy3)
        self.camera_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.camera_lbl)

        self.camera_box = QComboBox(self.CameraFrame)
        self.camera_box.setObjectName(u"camera_box")
        sizePolicy.setHeightForWidth(self.camera_box.sizePolicy().hasHeightForWidth())
        self.camera_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_25.addWidget(self.camera_box)


        self.verticalLayout_26.addWidget(self.CameraFrame)

        self.SettingsBtnFrame = QFrame(self.SettingOptionFrame)
        self.SettingsBtnFrame.setObjectName(u"SettingsBtnFrame")
        sizePolicy.setHeightForWidth(self.SettingsBtnFrame.sizePolicy().hasHeightForWidth())
        self.SettingsBtnFrame.setSizePolicy(sizePolicy)
        self.SettingsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.SettingsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.SettingsBtnFrame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.reset_btn = QPushButton(self.SettingsBtnFrame)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setStyleSheet(u"background-color: rgb(23, 107, 135);")

        self.horizontalLayout_26.addWidget(self.reset_btn)

        self.apply_btn = QPushButton(self.SettingsBtnFrame)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

        self.horizontalLayout_26.addWidget(self.apply_btn)


        self.verticalLayout_26.addWidget(self.SettingsBtnFrame)

        self.frame_7 = QFrame(self.SettingOptionFrame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.web_btn = QPushButton(self.frame_7)
        self.web_btn.setObjectName(u"web_btn")
        self.web_btn.setFlat(True)

        self.horizontalLayout_13.addWidget(self.web_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_26.addWidget(self.frame_7)


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
        self.label_7 = QLabel(self.ChangePINPage)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignLeft)

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

        self.horizontalLayout_6.addWidget(self.confirm_PIN_line)


        self.verticalLayout.addWidget(self.ConfirmPINFrame)

        self.change_PIN_hint_lbl = QLabel(self.ChangePINPage)
        self.change_PIN_hint_lbl.setObjectName(u"change_PIN_hint_lbl")
        sizePolicy6.setHeightForWidth(self.change_PIN_hint_lbl.sizePolicy().hasHeightForWidth())
        self.change_PIN_hint_lbl.setSizePolicy(sizePolicy6)
        self.change_PIN_hint_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.change_PIN_hint_lbl, 0, Qt.AlignHCenter)

        self.change_PIN_btn = QPushButton(self.ChangePINPage)
        self.change_PIN_btn.setObjectName(u"change_PIN_btn")
        sizePolicy4.setHeightForWidth(self.change_PIN_btn.sizePolicy().hasHeightForWidth())
        self.change_PIN_btn.setSizePolicy(sizePolicy4)
        self.change_PIN_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

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
        self.PIN_btn.setStyleSheet(u"background-color: rgb(100, 204, 197);")

        self.horizontalLayout_7.addWidget(self.PIN_btn)


        self.verticalLayout_4.addWidget(self.PINFrame, 0, Qt.AlignVCenter)

        self.PIN_checkbox = QCheckBox(self.PINValidationFrame)
        self.PIN_checkbox.setObjectName(u"PIN_checkbox")

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

        self.cont_stackedwidget.setCurrentIndex(1)
        self.use_time_btn.setDefault(False)
        self.PIN_stackedwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Align Position", None))
        self.logo_with_title_lbl.setText("")
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.parental_btn.setText(QCoreApplication.translate("MainWindow", u"  Parental Control", None))
        self.calibrate_btn.setText(QCoreApplication.translate("MainWindow", u"  Calibration", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.page_title_lbl.setText(QCoreApplication.translate("MainWindow", u"Page Title", None))
        self.min_btn.setText("")
        self.close_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Today Use Time:", None))
        self.use_time_lbl.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Monitoring", None))
        self.popout_btn.setText("")
        self.monitor_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.use_time_btn.setText(QCoreApplication.translate("MainWindow", u"Use Time", None))
        self.refresh_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.table_lbl.setText(QCoreApplication.translate("MainWindow", u"Computer Access Time", None))
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
        self.usetime_lbl.setText(QCoreApplication.translate("MainWindow", u"Total Use Time per day (h)", None))
        self.parental_box.setText(QCoreApplication.translate("MainWindow", u"Parental Option", None))
        self.usetime_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.other_lbl.setText(QCoreApplication.translate("MainWindow", u"Others", None))
        self.exct_data_btn.setText(QCoreApplication.translate("MainWindow", u"Extract All Data", None))
        self.restore_btn.setText(QCoreApplication.translate("MainWindow", u"Restore Data", None))
        self.changePIN_btn.setText(QCoreApplication.translate("MainWindow", u"Change PIN", None))
        self.calibrate_preview_lbl.setText("")
        self.calibrate_camera_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.hint_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.recalibrate_btn.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.proceed_btn.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.append_btn.setText(QCoreApplication.translate("MainWindow", u"Add Posture", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.start_box.setText(QCoreApplication.translate("MainWindow", u"Auto Start", None))
        self.background_box.setText(QCoreApplication.translate("MainWindow", u"Run In Background", None))
        self.app_time_track_box.setText(QCoreApplication.translate("MainWindow", u" App Use Time Tracking", None))
        self.reminder_lbl.setText(QCoreApplication.translate("MainWindow", u"Break Time (mins)", None))
        self.notify_box.setText(QCoreApplication.translate("MainWindow", u"Break Reminder", None))
        self.alert_lbl.setText(QCoreApplication.translate("MainWindow", u"Alert Position", None))
        self.alert_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Left", None))
        self.alert_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Right", None))

        self.camera_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.web_btn.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Create New PIN", None))
        self.old_PIN_lbl.setText(QCoreApplication.translate("MainWindow", u"Old PIN       ", None))
        self.new_PIN_lbl.setText(QCoreApplication.translate("MainWindow", u"New PIN     ", None))
        self.confirm_lbl.setText(QCoreApplication.translate("MainWindow", u"Confirm PIN", None))
        self.change_PIN_hint_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.change_PIN_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter your 6-digit PIN", None))
        self.PIN_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.PIN_checkbox.setText(QCoreApplication.translate("MainWindow", u"Remember for this launch", None))
        self.PIN_hint_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi
