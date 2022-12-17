# BitcoinAutotrading

Bitcoin autotrading HTS using Python and Bithumb APIs
  ![BTC_Auto_HTS](btcAuto_HTS.gif)

## Summary

- An automated Home Trading System (HTS) for Bitcoins. It uses Larry Williams(LW) Volatility Break-out strategy for back-testing and an API from one of Korean cryptocurrency exchange for real-time trading. 

## Motivation

- As cryptocurrency has been popular in the last decades, we targeted this short-term project to be an overall wrap up of our CS/DS knowledge with a taste of a hot tech-trend 

## Main Concepts

- Signal/Slot (Event Handling)
- Web APIs
- Websockets
- Investing Strategies (Moving-Average, L.W. Volatility Break-out strategy)

## Tools and APIs

1) PyQt & Qt Designer
- PyQt5 for graphic user interface (GUI)
- Qt Designer is used to build UIs with useful built-in widgets also with customized widgets
- PyQt also has its own straightforward event handling concept called Signal/Slot

2) Web APIs/Modules

- **Pybithumb** API from _Bithumb_
- Websocket (also included in **Pybithumb** API)

## Downside & Future Direction

- Need improvements on UI
- Actual run would hit breakpoints during sleep mode on the physical computer
  - Need to migrate to a server
- Need more update on investing strategy to handle constant votality
