import sys
from volatility import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import pybithumb

form_class = uic.loadUiType(
    "/Volumes/SteveJobs/localGit/bitcoin_tutorial/9_HTS/resource/main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ticker = "LUNA"
        self.button.clicked.connect(self.clickBtn)

        with open("/Volumes/SteveJobs/localGit/bitcoin_tutorial/bithumbKey.txt") as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            self.apiKey.setText(apikey)
            self.secKey.setText(seckey)

    def clickBtn(self):
        if self.button.text() == "Start Trading":
            apiKey = self.apiKey.text()
            secKey = self.secKey.text()
            if len(apiKey) != 32 or len(secKey) != 32:
                self.textEdit.append("Check the key again")
                return
            else:
                self.bithumb = pybithumb.Bithumb(apiKey, secKey)
                balance = self.bithumb.get_balance(self.ticker)
                if balance == None:
                    self.textEdit.append("Check the key again")
                    return
            self.button.setText("End Trading")
            self.textEdit.append("------ START ------")
            self.textEdit.append(f"Holding Cash: {balance[2]} won")
            self.vw = VolatilityWorker(self.ticker, self.bithumb)
            self.vw.tradingSent.connect(self.receiveTradingSignal)
            self.vw.start()
        else:
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
