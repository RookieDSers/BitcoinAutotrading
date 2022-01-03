## Websocket for Synchronization

- Use **Websocket Modules** to solve delays between request and response

### Using _Websocket_ module with _asyncio_ module

- Using _asyncio_ module:
    - Allows handle asynchronous operations
        ![syncho_vs_asyncho](syncho_vs_asyncho.png)
    - Use _run_ function to handle many **coroutines**(= async functions)
        ```python
        import asyncio 
        
        async def async_func1():
            print("Hello")
        
        asyncio.run(async_func1())
        ```
    - Use _await_ keyword when calling other coroutines in a coroutine
        ```python
        import asyncio 
        
        async def make_coffee():
            print("Coffee Start")
            await asyncio.sleep(3)
            print("Coffee End")
        
        async def make_tea():
            print("Tea Start")
            await asyncio.sleep(5)
            print("Tea End")
        
        async def main():
            coro1 = make_coffee()
            coro2 = make_tea()
            await asyncio.gather(
                coro1, 
                coro2
            )
        
        print("Main Start")
        asyncio.run(main())
        print("Main End")


        ###### Result ######
        
        Main Start
        Coffee Start
        Tea Start
        Coffee End
        Tea End
        Main End
        ```

    - Coroutine can also return values
        ```python
        async def make_coffee():
            ...
            return "Coffee"
        
        async def make_tea():
            ...
            return "Tea"
        
        async def main():
            ...
            result = await asyncio.gather(
                coro1,
                coro2
            )
            print(result)
        ```
- Use _multiprocessing_ module to handle multiple events
    - Use _queue_ to send data to another process
        ```python
        import multiprocessing as mp

        q = mp.Queue()
        ```
    - Spawn a subprocess to handle coroutine and data with the _queue_
        ```python
        p = mp.Process(name="Producer", target=producer, args=(q,), daemon=True)
        p.start()
        ```

- Coroutine: subscribe _Bithumb_ website to receive real-time coin data
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

    ![websocket_module](websocket_module.gif)

### Using _pybithumb_ module to handle websocket
- Use _pybithumb_ built-in _WebSocketManager_:
    - receives data from _Bithumb_ server
    - handle and put the data into _queue_
    ```python
    from pybithumb import WebSocketManager
    ...

    class Worker(QThread):
        recv = pyqtSignal(str)

        def run(self):
            # create websocket for Bithumb
            wm = WebSocketManager("ticker", ["BTC_KRW"])
            while True:
                # take the data out from the queue
                data = wm.get()
                self.recv.emit(data['content']['closePrice'])
    ```
    ![pybithumb_websocket](pybithumb_websocket.gif)