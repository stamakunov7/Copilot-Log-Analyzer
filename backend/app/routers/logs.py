from fastapi import APIRouter, Depends
from ..schemas import LogEventIn
from ..database import get_db

router = APIRouter()

@router.post("/", status_code=201)
async def create_log(log: LogEventIn, db=Depends(get_db)):
    return {"status": "received", "log": log.dict()}

@router.post("/batch", status_code=201)
async def batch_logs(logs: list[LogEventIn], db=Depends(get_db)):
    return {"received": len(logs)}
