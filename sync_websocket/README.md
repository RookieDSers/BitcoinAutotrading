## Websocket for Synchronization

- Use **Websocket Modules** to solve delays between request and response

### Using _Websocket_ Module
- Subscribe _Bithumb_ website to receive real-time data of crypto coins
    ```python
    async def bithumb_ws_clinet(q):
        # receive coin data with websocket, and put into a Queue

        uri = "wss://pubwss.bithumb.com/pub/ws"

        # set ping_interval as None to stop sending Ping frame to Bithumb server
        async with websockets.connect(uri, ping_interval=None) as websocket:

            # set the request format as JSON (<-dictionary)
            subscribe_fmt = {
                "type": "ticker",
                "symbols": ["BTC_KRW"],
                "tickTypes": ["1H"]
            }
            subscribe_data = json.dumps(subscribe_fmt)
            await websocket.send(subscribe_data)

            while True:
                # recieve data form the server
                data = await websocket.recv()
                data = json.loads(data)
                q.put(data)
    ```
