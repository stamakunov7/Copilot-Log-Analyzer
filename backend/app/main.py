import json
from typing import Optional

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.middleware.cors import CORSMiddleware

from .routers import logs, sessions, summaries, metrics

app = FastAPI(title="Copilot Log Analyzer - Backend")

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(logs.router, prefix="/api/logs")
app.include_router(sessions.router, prefix="/api/sessions")
app.include_router(summaries.router, prefix="/api/sessions/{session_id}/summaries")
app.include_router(metrics.router, prefix="/api/sessions/{session_id}/metrics")

@app.get("/health")
async def health_check():
    # Simple health check, to verify the server is running
    return {"status": "ok"}

@app.websocket("/ws/logs")
async def websocket_endpoint(
    websocket: WebSocket,
    session_id: str = Query(..., description="The ID of the session to stream logs for"),
    project: Optional[str] = Query(None, description="Project name associated with the logs"),
):
    await websocket.accept()
    print(f"[WS] Connected: session_id={session_id}, project={project}")

    try:
        while True:
            data = await websocket.receive_text()

            try:
                payload = json.loads(data)
            except json.JSONDecodeError:
                print(f"[WS] ({session_id}) invalid JSON: {data!r}")
                # We could send an error back to client here if needed
                continue

            level = payload.get("level", "INFO")
            message = payload.get("message", "")
            ts = payload.get("timestamp", "")

            # For now, just log to stdout (later we'll write to DB)
            print(f"[WS] ({session_id}) [{level}] {ts} {message}")

            # We could send an ack back to client if needed:
            # await websocket.send_json({"status": "ok"})

    except WebSocketDisconnect:
        print(f"[WS] Disconnected: session_id={session_id}")
    except Exception as e:
        print(f"[WS] Error in connection {session_id}: {e}")
        # In the future, we could log this to a separate error log
        await websocket.close()
