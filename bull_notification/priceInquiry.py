import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pybithumb

form_class = uic.loadUiType("/Volumes/SteveJobs/Projects/BitcoinAutotrading/PyQt+pybithumb/window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # price inquiry whenever clicked
        # self.pushButton.clicked.connect(self.inquiry)

        self.timer = QTimer(self)       # create QTimer instance
        self.timer.start(1000)          # set inverval as 1000ms = 1 sec
        self.timer.timeout.connect(self.inquiry)    # even loop in every second

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pybithumb.get_current_price("BTC")
        self.lineEdit.setText(str(price))


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
