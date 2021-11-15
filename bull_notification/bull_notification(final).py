import pybithumb

# Get 5-Day SMA
def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

# Get Base Price with Volatility Strategy (K=0.5)
def get_base_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    base = today_open + (yesterday_high - yesterday_low) * 0.5
    return base

# Classify whether Bull or Bid of a ticker
def is_bull_market(ticker):
    ma5 = get_yesterday_ma5(ticker)
    base = get_base_price(ticker)
    price = pybithumb.get_current_price(ticker)
    if price > ma5 and price > base:
        return True
    else:
        return False

# Check ticker's bull/bid market
tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = is_bull_market(ticker)
    if is_bull:
        print(ticker, " is Bull!!!")
    else:
        print(ticker, " is Bear...")
