from ..models import LogEvent

async def ingest_log(db, log_in):
    # placeholder: create and persist LogEvent
    le = LogEvent(session_id=log_in.session_id, level=log_in.level, message=log_in.message)
    db.add(le)
    await db.commit()
    await db.refresh(le)
    return le
