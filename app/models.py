from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from app.database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    content = Column(Text, nullable=True)
    reminder_at = Column(DateTime, nullable=True)
    priority = Column(String(20), default="Medium", nullable=False)
    tag = Column(String(50), default="General", nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)