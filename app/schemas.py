from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    content: Optional[str] = None
    reminder_at: Optional[datetime] = None
    priority: str = Field(default="Medium", pattern="^(Low|Medium|High)$")
    tag: str = Field(default="General", max_length=50)


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=150)
    content: Optional[str] = None
    reminder_at: Optional[datetime] = None
    priority: Optional[str] = Field(default=None, pattern="^(Low|Medium|High)$")
    tag: Optional[str] = Field(default=None, max_length=50)
    is_completed: Optional[bool] = None


class NoteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: Optional[str]
    reminder_at: Optional[datetime]
    priority: str
    tag: str
    is_completed: bool
    created_at: datetime
