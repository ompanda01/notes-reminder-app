from datetime import datetime
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Note
from app.schemas import NoteCreate, NoteUpdate, NoteResponse
from app.ai_helper import infer_priority_and_tag

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Notes + Reminder API", version="0.1.0")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_INDEX = BASE_DIR / "frontend" / "index.html"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_INDEX)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Smart Notes + Reminder API is running"}


@app.post("/notes", response_model=NoteResponse, status_code=201)
def create_note(note_in: NoteCreate, db: Session = Depends(get_db)):
    try:
        inferred_priority, inferred_tag = infer_priority_and_tag(note_in.title, note_in.content)
    except TypeError:
        inferred_priority, inferred_tag = infer_priority_and_tag(note_in.title)

    priority = (
        inferred_priority
        if (not note_in.priority or note_in.priority == "Medium")
        else note_in.priority
    )
    tag = (
        inferred_tag
        if (not note_in.tag or note_in.tag == "General")
        else note_in.tag
    )

    note = Note(
        title=note_in.title,
        content=note_in.content,
        priority=priority,
        tag=tag,
        reminder_at=note_in.reminder_at,
        is_pinned=note_in.is_pinned,
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@app.get("/notes", response_model=List[NoteResponse])
def list_notes(
    priority: Optional[str] = Query(default=None),
    is_completed: Optional[bool] = Query(default=None),
    is_pinned: Optional[bool] = Query(default=None),
    tag: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Note)
    if priority:
        query = query.filter(Note.priority == priority)
    if is_completed is not None:
        query = query.filter(Note.is_completed == is_completed)
    if is_pinned is not None:
        query = query.filter(Note.is_pinned == is_pinned)
    if tag:
        query = query.filter(Note.tag == tag)
    return query.order_by(Note.is_pinned.desc(), Note.id.desc()).all()


@app.get("/reminders/upcoming", response_model=List[NoteResponse])
def upcoming_reminders(within_hours: int = 24, db: Session = Depends(get_db)):
    now = datetime.utcnow()
    return (
        db.query(Note)
        .filter(Note.reminder_at.isnot(None), Note.reminder_at >= now, Note.is_completed == False)
        .order_by(Note.reminder_at.asc())
        .all()
    )


@app.patch("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_in: NoteUpdate, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    update_data = note_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(note, field, value)
    db.commit()
    db.refresh(note)
    return note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"deleted": True, "id": note_id}