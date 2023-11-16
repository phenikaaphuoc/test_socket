import asyncio
import websockets

async def handle_connection(websocket, path):
    # Handle incoming messages from the client
    async for message in websocket:
        print(f"Received message: {message}")

        # Send a response back to the client
        response = f"Server received: {message}"
        await websocket.send(response)

# Start the WebSocket server
start_server = websockets.serve(handle_connection, "0.0.0.0", 8765)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
