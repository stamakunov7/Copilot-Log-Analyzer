from fastapi import FastAPI

from .routers import logs, sessions, summaries, metrics

app = FastAPI(title="Copilot Log Analyzer - Backend")

app.include_router(logs.router, prefix="/api/logs")
app.include_router(sessions.router, prefix="/api/sessions")
app.include_router(summaries.router, prefix="/api/sessions/{session_id}/summaries")
app.include_router(metrics.router, prefix="/api/sessions/{session_id}/metrics")

@app.get("/health")
async def health():
    return {"status": "ok"}
