import pybithumb
import time

keys = []
with open('.../bithumbKey.txt') as f:
    keys = f.readlines()
bithumb = pybithumb.Bithumb(keys[0].strip(), keys[1].strip())

# check balance
for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    print(ticker, ':', balance)
    time.sleep(0.1)
