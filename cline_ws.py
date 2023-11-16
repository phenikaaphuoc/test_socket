import asyncio
import websockets
import time
async def connect_to_server():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        while True:
            message = input("Nhap input")
            if message == "q":
                break
            t = time.time()
            await websocket.send(message)
            print(f"Sent message: {message}")
            print(time.time()-t)
            # Receive and print the server's response
            response = await websocket.recv()
            print(f"Received response: {response}")
            print(time.time()-t)

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_server())
