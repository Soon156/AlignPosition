from PySide6.QtWidgets import QVBoxLayout, QWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime

from Funtionality.Config import bright_colors_light_blue_theme, GRAY_COLOR, dark_colors_purple_theme
from ParentalControl.Auth import read_use_time


class UseTimeChartWidget(QWidget):
    def __init__(self, theme):
        super().__init__()
        self.recent_annotation = None
        self.theme = theme
        self.init_ui()

    def init_ui(self):

        # Extract data for the chart
        rows = read_use_time()
        rows.reverse()

        categories = []
        values = []
        for item in rows[:7]:
            date_str, value = item[0], float(item[1]) / 60
            categories.append(datetime.strptime(item[0], "%Y-%m-%d").strftime("%b %d"))
            values.append(value)

        values.reverse()
        categories.reverse()

        # Create a Matplotlib bar chart
        self.figure, self.ax = plt.subplots(figsize=(6.5, 3))
        if self.theme:
            self.ax.bar(categories, values, color=bright_colors_light_blue_theme)
            self.ax.tick_params(axis='both', colors=GRAY_COLOR)
        else:
            self.figure.set_facecolor('#2B2D36')
            self.ax.set_facecolor('#2B2D36')
            self.ax.bar(categories, values, color=dark_colors_purple_theme)
            self.ax.tick_params(axis='both', colors='white')

        self.ax.set_ylabel('Use Time (mins)')
        self.ax.set_title('Total Use Time')
        self.figure.tight_layout()

        # Embed Matplotlib plot in PyQt widget
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.cid = self.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def on_hover(self, event):
        if event.inaxes == self.ax:
            for bar, value in zip(self.ax.patches, self.ax.patches):
                if bar.contains(event)[0]:
                    x, y = bar.get_xy()
                    height = bar.get_height()
                    annotation = self.ax.annotate(f'{value.get_height():.2f} mins', (x + bar.get_width() / 2, height),
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
