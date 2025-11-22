from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_summaries(session_id: int):
    return []

@router.post("/generate")
async def generate_summary(session_id: int):
    return {"summary": "not implemented"}
