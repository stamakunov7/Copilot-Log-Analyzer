from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_sessions():
    return []

@router.get("/{session_id}")
async def get_session(session_id: int):
    return {"id": session_id}
