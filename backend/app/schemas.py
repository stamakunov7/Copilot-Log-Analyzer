from pydantic import BaseModel
from typing import Optional, Any
import datetime

class LogEventIn(BaseModel):
    session_id: int
    level: str
    message: str
    meta: Optional[Any] = None
    timestamp: Optional[datetime.datetime] = None

class SessionOut(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime

class SummaryOut(BaseModel):
    id: int
    session_id: int
    text: str
    created_at: datetime.datetime
