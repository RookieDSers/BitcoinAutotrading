import sys
from volatility import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import pybithumb

form_class = uic.loadUiType("resource/main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ticker = "BTC"
        self.button.clicked.connect(self.clickBtn)

        # read and fill in private keys from .txt file
        with open("bithumbKey.txt") as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            self.apiKey.setText(apikey)
            self.secKey.setText(seckey)
    
    # button click action
    def clickBtn(self):
        if self.button.text() == "Start Trading":
            apiKey = self.apiKey.text()
            secKey = self.secKey.text()
            
            # check validity of the private keys
            if len(apiKey) != 32 or len(secKey) != 32:
                self.textEdit.append("Check the key again")
                return
            else: 
                # check the current balance
                self.bithumb = pybithumb.Bithumb(apiKey, secKey)
                balance = self.bithumb.get_balance(self.ticker)
                if balance == None:
                    self.textEdit.append("Check the key again")
                    return
            
            # change button and (add) textEdit displays
            self.button.setText("End Trading")
            self.textEdit.append("------ START ------")
            self.textEdit.append(f"Holding Cash: {balance[2]} won")
            
            # connect slot with the generated signal
            self.vw = VolatilityWorker(self.ticker, self.bithumb)
            self.vw.tradingSent.connect(self.receiveTradingSignal)
            self.vw.start()
        else:
            # end auto-trading
            self.vw.close()
            self.textEdit.append("------ END ------")
            self.button.setText("Start Trading")

    def receiveTradingSignal(self, time, type, amount):
        self.textEdit.append(f"[{time}] {type} : {amount}")

    def closeEvent(self, event):
        try:
            self.vw.close()
        except:
            pass
        self.widget.closeEvent(event)
        self.widget_2.closeEvent(event)
        self.widget_3.closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
