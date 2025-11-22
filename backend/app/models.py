from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class LogEvent(Base):
    __tablename__ = "log_events"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, nullable=False)
    level = Column(String)
    message = Column(String)
    meta = Column(JSON)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, nullable=False)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
