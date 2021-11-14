import pybithumb

# Get detail data for each date
btc = pybithumb.get_ohlcv("BTC")  # returns DataFrame
print(btc)
close = btc['close']
print('close:')
print(close)

# Calculate "Moving Average"
window = close.rolling(5)   # group the data with size 5
ma5 = window.mean()
print(ma5)

# Bull notification
last_ma5 = ma5[-2]
price = pybithumb.get_current_price("BTC")

if price > last_ma5:
    print("Bull!!!")
else:
    print("Bear...")

### Define Bull notification function ###


def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df.rolling(5).mean()
    price = pybithumb.get_current_price(ticker)
    last_ma5 = ma5[-2]
    if price > last_ma5:
        return True
    else:
        return False


tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker, " is Bull!!!")
    else:
        print(ticker, " is Bear...")
