import sys

from PyQt5.QtChart import QChart, QLineSeries, QChartView
from PyQt5.QtCore import QPointF

from qtpy.QtWidgets import QVBoxLayout, QPushButton, QErrorMessage, \
    QApplication, QWidget, QHBoxLayout, QGridLayout, QListWidget, QMainWindow

from model.resourcemanager import ResourceManager


class Form(QWidget):

    def __init__(self, parent=None):

        super(Form, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)

        h_layout = QHBoxLayout()
        self.list = QListWidget()
        self.list.resize(20,50)
        h_layout.addWidget(self.list)

        manager = ResourceManager()
        self.data = manager.run(100)

        self.grid = QGridLayout(self)
        self.grid.addLayout(self.layout, 0, 0, 4, 4)
        self.grid.addLayout(h_layout, 0, 2, 1, 1)

        for key, value in self.data.items():
            self.list.addItem(key)

        self.setLayout(self.grid)

        self.list.currentTextChanged.connect(self.rewrite_data)

    def rewrite_data(self, args):

        self.layout = QVBoxLayout()
        self.grid.addLayout(self.layout, 0, 0, 1, 1)
        for key, value in self.data[args].items():
            chart = QChart()
            chart_view = QChartView(chart)
            series = QLineSeries()
            series.setName(key)

            for i in value:
                series.append(QPointF(i[0], i[1]))

            chart.addSeries(series)
            chart.createDefaultAxes()
            self.layout.addWidget(chart_view)

    def start(self):
        self.message('Настройти до конца')

    def message(self, message):
        error = QErrorMessage(self)
        error.showMessage(message)

main = QApplication(sys.argv)
my_win = Form()
my_win.show()
sys.exit(main.exec_())