import asyncio
import websockets
import time

# start the websocket client
async def start_client():
    async with websockets.connect("ws://localhost:80/ws") as websocket:
        while True:
            inp = input("Nhap vao message:")
            if inp == "q":
                break
            t = time.time()
            await websocket.send(inp)
            print(time.time()-t)
            message = await websocket.recv()
            print(time.time()-t)
            print(message)


# run the client
asyncio.run(start_client())