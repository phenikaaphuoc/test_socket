from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
app = FastAPI()
clients = []
import uvicorn

async def handle_message(websocket: WebSocket):

    global fastest_time
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(f"your message is {message}")
            if message == "dis":
                return
    except WebSocketDisconnect:
        pass

# WebSocket route
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await handle_message(websocket)

@app.get("/")
async  def hello():
    return {"myhome"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
