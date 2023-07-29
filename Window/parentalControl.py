from PySide6 import QtCharts
from PySide6.QtCharts import QBarSet, QBarSeries, QBarCategoryAxis, QChart
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QDialog, QSizePolicy
from PySide6.QtCore import Signal, Qt, QSize

from Funtionality.EncryptData import read_use_time
from UI.ui_parentalControl import Ui_ParentalControlDialog
import logging as log

# Import your data here (replace this with your actual data)
data = [(1, 10), (2, 20), (3, 15), (4, 30)]
# TODO different view, today, week, month

rows = read_use_time()


class ParentalWindow(QDialog, Ui_ParentalControlDialog):
    configReset = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = None
        self.setupUi(self)
        self.rows = rows
        self.chart_view = None
        self.create_chart()
        self.tut_lbl.setText("Total Use Time")
        self.index = 0
        self.put_btn.clicked.connect(self.change_page)
        self.tut_btn.clicked.connect(self.change_page)

        # Call the function to update the chart with data
        # self.update_chart()
    def change_page(self):
        if self.index == 0:
            self.stackedWidget.setCurrentIndex(1)
            self.index = 1
        else:
            self.stackedWidget.setCurrentIndex(0)
            self.index = 0

    def create_chart(self):
        # Create a single QBarSet to hold the data values
        bar_set = QBarSet("Data Values")
        categories = []
        # Add data values to the bar_set
        for item in rows[:7]:
            bar_set.append(item[1]/60)
            categories.append(item[0])

        # Create a QBarSeries and add the bar_set to it
        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        # chart.setTitle("Total Use Time")

        # Set up the X-axis with the date categories
        axis = QBarCategoryAxis()
        axis.append(categories)

        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        y_axis = chart.axisY()
        y_axis.setLabelFormat("%02d")
        y_axis.setTitleText("Use Time (min)")

        chart.legend().setVisible(False)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view = QtCharts.QChartView(chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        # self.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # size_policy.setHorizontalStretch(0)
        # size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.chart_view.sizePolicy().hasHeightForWidth())
        self.chart_view.setSizePolicy(size_policy)

        self.chart_view.setMinimumSize(QSize(0, 300))
        self.tut_cont.addWidget(self.chart_view)


"""        
Stacked bar
for item in rows:
            categories.append(item[0])
            setattr(self, "set" + str(item[0]), QtCharts.QBarSet(str(item[0])))
            series.append((getattr(self, "set" + str(item[0]))))
            getattr(self, "set" + str(item[0])).append(item[1])
"""