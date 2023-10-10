from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from services.connection_manager import ConnectionManager
import time

chat_route = APIRouter(prefix="/chat", tags=["Chat"])

manager = ConnectionManager()


@chat_route.websocket("/{chat_uid}")
async def websocket_endpoint(websocket: WebSocket, chat_uid: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{chat_uid} left the chat")
