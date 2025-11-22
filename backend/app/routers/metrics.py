from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_metrics(session_id: int):
    return {"p90": None, "p99": None}
