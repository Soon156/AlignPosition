from numpy import sum
from PySide6.QtWidgets import QVBoxLayout, QWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from Funtionality.Config import GRAY_COLOR, STRING_LIMIT
from ParentalControl.Auth import read_app_use_time


class ProgramUseTimeChartWidget(QWidget):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.cid = None
        self.ax = None
        self.figure = None
        self.canvas = None
        self.app_use_time_list = []
        self.app_total_use_time_with_name = []
        self.recent_annotation = None
        self.date_list = []
        self.app_use_time_per_day = {}
        self.init_chart()
        self.init_ui()

    def init_ui(self):
        # Create a Matplotlib bar chart
        self.figure, self.ax = plt.subplots(figsize=(9, 3))

        for i, (app, use_time) in enumerate(zip(self.app_total_use_time_with_name, self.app_use_time_list)):
            if i == 0:
                self.ax.bar(self.date_list, use_time, label=app)
            else:
                bottom = sum(self.app_use_time_list[:i], axis=0)
                self.ax.bar(self.date_list, use_time, bottom=bottom, label=app)

        if self.theme:
            self.ax.tick_params(axis='both', colors=GRAY_COLOR)
        else:
            self.figure.set_facecolor('#2B2D36')
            self.ax.set_facecolor('#2B2D36')
            self.ax.tick_params(axis='both', colors='white')

        # Customize color for the legend
        self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False, facecolor='none',
                       edgecolor='none')
        self.ax.set_title('Program Use Time')
        self.ax.set_xlim(-1, len(self.date_list))
        max_value = 0

        for key, value in self.app_use_time_per_day.items():
            if value > max_value:
                max_value = value
        if max_value > 0:
            self.ax.set_ylim(0, max_value * 115/100)
        self.figure.tight_layout()

        # Embed Matplotlib plot in PyQt widget
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.cid = self.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def init_chart(self):
        # Extract data for the chart
        data = read_app_use_time()
        sorted_dates = sorted(data.keys(), key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

        # Calculate the total time for each app
        app_total_time = {}

        for date in sorted_dates[-7:]:
            formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%b %d")
            self.date_list.append(formatted_date)
            self.app_use_time_per_day[formatted_date] = 0
            for app in data[date]:
                app_total_time[app] = app_total_time.get(app, 0) + data[date][app]
        # Sort the apps based on total time in descending order
        sorted_apps = sorted(app_total_time.items(), key=lambda x: x[1], reverse=True)

        for app, total_time in sorted_apps[:7]:
            if len(app) > STRING_LIMIT:
                app = app[:STRING_LIMIT] + '...'
            name = f"{app}: {round(total_time / 60, 2)} mins"
            self.app_total_use_time_with_name.append(name)

        # Add the use time list of app to the bar
        top_7_apps = [app for app, _ in sorted_apps[:7]]
        for app in top_7_apps:
            usetime_for_the_same_app = []
            for date in sorted_dates[-7:]:
                use_timedate = 0
                if app in data[date]:
                    use_timedate = round(data[date][app] / 60, 2)
                    self.app_use_time_per_day[datetime.strptime(date, "%Y-%m-%d").strftime("%b %d")] += use_timedate
                usetime_for_the_same_app.append(use_timedate)
            self.app_use_time_list.append(usetime_for_the_same_app)

    def on_hover(self, event):
        if event.inaxes == self.ax:
            for bar, value in zip(self.ax.patches, self.ax.patches):
                if bar.contains(event)[0]:
                    x, y = bar.get_xy()
                    # Calculate the category index based on the bar's x position
                    category_index = round(x)
                    category_labels = self.ax.get_xticklabels()  # Assuming your x-axis has labels
                    category = category_labels[category_index].get_text()
                    annotation = self.ax.annotate(f'{value.get_height():.2f} mins',
                                                  xy=(x + bar.get_width() / 2, self.app_use_time_per_day[category]),
                                                  ha='center', va='center', xytext=(0, 10), textcoords='offset points')

                    # Remove the recent annotation
                    if self.recent_annotation:
                        self.recent_annotation.remove()

                    self.recent_annotation = annotation
                    break

            else:
                # Remove the recent annotation when not focused on any bar
                if self.recent_annotation:
                    self.recent_annotation.remove()
                    self.recent_annotation = None

        self.canvas.draw()
