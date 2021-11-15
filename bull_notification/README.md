## Bull Notification

### Real Time Price Inquiry

- Use QTimer, QTime for real time GUI

  ```python
  # in MyWindow constructor
  self.timer = QTimer(self)       # create QTimer instance
  self.timer.start(1000)          # set inverval as 1000ms = 1 sec
  self.timer.timeout.connect(self.inquiry)    # even loop in every second

  # make an inquiry every second and display tima and updated BTC price
  def inquiry(self):
      cur_time = QTime.currentTime()
      str_time = cur_time.toString("hh:mm:ss")
      self.statusBar().showMessage(str_time)
      price = pybithumb.get_current_price("BTC")
      self.lineEdit.setText(str(price))
  ```

  ![Price Inquiry](/bull_notification/price_inquiry.gif)

---

### Moving Average Method

- Classify bull/bid market with **Simple Moving Average(SMA)**
- _N_ Day-Moving Average:
  $$ ma5 = P*{i-5} + P*{i-4} + ... + P*{i-1}$$
  ($P*{i-k}$ is closing price of k days before current day)
- We applied 5 Day-Moving Average
- Reference:
  - https://corporatefinanceinstitute.com/resources/knowledge/other/moving-average/
  - https://wikidocs.net/21882

---

### Moving Average in Python codes

1. Get closing price data of ticker for each date

```python
  import pybithumb
  btc = pybithumb.get_ohlcv("BTC")
  print(btc)
  close = btc['close']
  print('close:')
  print(close)
```

2. Get five days moving average

```python
  window = close.rolling(5)
  ma5 = window.mean()
  print(ma5)
```

3. Define bull market and bear market based on the moving average of last five days. If the current price is higher than the moving average of last five days, then it's bull market, otherwise it's bear market

```python
  last_ma5 = ma5[-2]
  price = pybithumb.get_current_price("BTC")
  if price > last_ma5:
      print("Bull!!!")
  else:
      print("Bear...")
```

4. Define function with the above codes

```python
  def bull_market(ticker):
      df = pybithumb.get_ohlcv(ticker)
      ma5 = df.rolling(5).mean()
      price = pybithumb.get_current_price(ticker)
      last_ma5 = ma5[-2]
      if price > last_ma5:
          return True
      else:
          return False
```

5. Decide all tickers' market depends on the moving average strategy defined above

```python
  tickers = pybithumb.get_tickers()
  for ticker in tickers:
      is_bull = bull_market(ticker)
      if is_bull:
          print(ticker, " is Bull!!!")
      else:
          print(ticker, " is Bear...")
```

---

### Moving Average in PyQt

- Set initial _tickers_
  ```python
  tickers = ["BTC", "ETH", "BCH", "ETC"]
  ```
- Set up QTable elements in the constructor

  ```python
  class MyWindow(QMainWindow, form_class):
    def __init__(self):
        ...
        # set rowNum to tickers
        self.tableWidget.setRowCount(len(tickers))

        # set up each ticker's data to each cell
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

        # set up timer for real time update (every 5sec)
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)
  ```

- Get each ticker's data and classification of whether a ticker is bull or bear (apply python code)

  ```python
  def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None
        if price > last_ma5:
            state = "Bull!!!"
        else:
            state = "Bear..."

        return price, last_ma5, state
  ```

- Update each ticker's info on Qtable

  ```python
  def timeout(self):
        for i, ticker in enumerate(tickers):
            price, last_ma5, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(state))
  ```

  ![MovingAveragePyQt](/bull_notification/ma5.gif)

---

### Volatility Breakout Strategy

- We applied **Volatility Breakout Strategy** (_by Larry Williams_) to make our bull/bid classification more appropirate.

  1. Calculate the Range:

  ```
  Range = Daily High - Daily Low
  ```

  2. Set Base Price with constant _K_(_noise ratio_):

  ```
  Base Price = Previous Day's Candle Close + (Range * K)
  ```

  3. When today's price exceeds base price, enter a position

  4. Next day, sell all the positions at the daily open price

- We've set our initial noise ratio(_K_) as 0.5

- Reference:
  - https://www.tradingview.com/chart/TSLA/vlvAMwqN-Volatility-Breakout-Trading-Explained/
  - https://wikidocs.net/21888

---

### Volatility Breakout in Python codes

1. Calculate base price with the k value of .5

```python
df = pybithumb.get_ohlcv("BTC")
yesterday = df.iloc[-2]
today_open = yesterday['close']
yesterday_high = yesterday['high']
yesterday_low = yesterday['low']
base = today_open + (yesterday_high - yesterday_low) * 0.5
print(base)
```

2. Define bull notification based on the base price

```python
price = pybithumb.get_current_price("BTC")

if price > base:
    print("Bull!!!")
else:
    print("Bear...")
```

3. Define the above codes as function

```python
def vol_bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    base = today_open + (yesterday_high - yesterday_low) * 0.5
    price = pybithumb.get_current_price(ticker)
    if price > base:
        return True
    else:
        return False
```

4. Define all tickers' bull notification with the above function

```python
tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = vol_bull_market(ticker)
    if is_bull:
        print(ticker, " is Bull!!!")
    else:
        print(ticker, " is Bear...")
```

---

### Final Version for Bull Notification

1. Define the functions calculating both 5-day SMA and base price

```python
def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

def get_base_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    base = today_open + (yesterday_high - yesterday_low) * 0.5
    return base

```

2. Define the final function of bull notification with the strategies above

```python
def is_bull_market(ticker):
    ma5 = get_yesterday_ma5(ticker)
    base = get_base_price(ticker)
    price = pybithumb.get_current_price(ticker)
    if price > ma5 and price > base:
        return True
    else:
        return False
```

---

### Bull/Bid Notifiaction PyQt

- update instance function with two metods above:

  ```python
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

        # Get current price of a ticker
        price = pybithumb.get_current_price(ticker)
        state = None

        # Classify based on two target prices above
        if price > last_ma5 and price > base:
            state = "Bull!!!"
        else:
            state = "Bear..."

        return price, last_ma5, base, state
  ```

  ![Notification](/bull_notification/notification.gif)
