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

### Moving Average in PyQt

### Volatility Breakout Strategy

### Volatility Breakout in Python codes

### Final Version for Bull Notification

### Bull/Bid Notifiaction PyQt
