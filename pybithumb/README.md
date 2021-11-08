## What is Bithumb and pybithumb?

---
### Introduction to Bithumb
- [Bithumb](https://en.bithumb.com/) is a South Korean cryptocurrency exchange founded in 2014.
- Bithumb is one of the most actively used cryptocurrency exchange in South Korea with over 8M registered users and 1M mobile app users.
- Current transaction volume through the Bithumb has exceeded 1 trillion USD.
---
### Introduction to pybithumb
- we used pybithumb module provided by Bithumb.
- Referenced: [pybithumb public and private API](https://apidocs.bithumb.com/docs/api_info)
---
### Introduction to pybithumb functions (public API)
| Function | Description |
| --- | --- |
| pybithumb.get_tickers() | return all tickers that are being traded in bithumb|
| pybithumb.get_current_price(_ticker_) | return the current price of input ticker |
| pybithumb.get_market_detail(_ticker_) | return tuple with lowest price, highest price, average price, and trading volume of input ticker|
| pybithumb.get_orderbook(_ticker_) | return dictionary with 5 keys (timestamp, payment_currency, order_currency, bids, asks)|
---
### Introduction to bithumb functions (private API)
| Function | Description |
| --- | --- |
| pybithumb.Bithumb(apiKey, secretKey) | get user information (api and secret keys) |
| bithumb.get_balance(_ticker_) | return the current balance in user's account |

