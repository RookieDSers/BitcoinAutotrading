
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

form_class = uic.loadUiType(
    "/Volumes/SteveJobs/Projects/BitcoinAutotrading/bull_notification/notification.ui")[0]
tickers = ["BTC", "ETH", "BCH", "ETC"]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setRowCount(len(tickers))
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)
    
    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        
        # Get ma5
        close = df['close']
        ma5 = close.rolling(5).mean()
        last_ma5 = ma5[-2]
        
        # Get base price
        yesterday = df.iloc[-2]
        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        base = today_open + (yesterday_high - yesterday_low) * 0.5
        
        price = pybithumb.get_current_price(ticker)

        state = None
        if price > last_ma5 and price > base:
            state = "Bull!!!"
        else:
            state = "Bear..."

        return price, last_ma5, base, state

    def timeout(self):
        for i, ticker in enumerate(tickers):
            # item = QTableWidgetItem(ticker)
            # self.tableWidget.setItem(i, 0, item)

            price, last_ma5, base, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(base)))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(state))


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
