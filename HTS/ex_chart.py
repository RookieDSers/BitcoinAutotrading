import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtChart import QLineSeries, QChart
from PyQt5.QtGui import QPainter


class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi(
            "/Volumes/SteveJobs/localGit/bitcoin_tutorial/9_HTS/resource/chart.ui", self)
        self.ticker = ticker

        # limit the data number to 120
        self.viewLimit = 120

        # set chart data sample
        self.priceData = QLineSeries()
        self.priceData.append(0, 10)
        self.priceData.append(1, 20)
        self.priceData.append(2, 10)

        # put the charData to QChart
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)

        # set chart view
        self.priceView.setChart(self.priceChart)

        # hide legend and antialiase graph
        self.priceChart.legend().hide()
        self.priceView.setRenderHints(QPainter.Antialiasing)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())
