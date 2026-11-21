from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Note
from app.schemas import NoteCreate, NoteUpdate, NoteResponse
from app.ai_helper import infer_priority_and_tag

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Notes + Reminder API", version="0.1.0")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Smart Notes + Reminder API is running"}


@app.post("/notes", response_model=NoteResponse, status_code=201)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    auto_priority, auto_tag = infer_priority_and_tag(payload.title, payload.content)
    priority = payload.priority if payload.priority != "Medium" else auto_priority
    tag = payload.tag if payload.tag != "General" else auto_tag

    note = Note(
        title=payload.title,
        content=payload.content,
        reminder_at=payload.reminder_at,
        priority=priority,
        tag=tag,
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@app.get("/notes", response_model=List[NoteResponse])
def list_notes(
    tag: Optional[str] = None,
    priority: Optional[str] = None,
    is_completed: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Note)
    if tag:
        query = query.filter(Note.tag == tag)
    if priority:
        query = query.filter(Note.priority == priority)
    if is_completed is not None:
        query = query.filter(Note.is_completed == is_completed)
    return query.order_by(Note.created_at.desc()).all()


@app.get("/reminders/upcoming", response_model=List[NoteResponse])
def upcoming_reminders(
    within_hours: int = Query(default=24, ge=1, le=720),
    db: Session = Depends(get_db),
):
    now = datetime.utcnow()
    notes = (
        db.query(Note)
        .filter(
            Note.reminder_at.isnot(None),
            Note.is_completed.is_(False),
            Note.reminder_at >= now,
        )
        .order_by(Note.reminder_at.asc())
        .all()
    )
    return [
        n for n in notes
        if n.reminder_at and (n.reminder_at - now).total_seconds() <= within_hours * 3600
    ]


@app.patch("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, payload: NoteUpdate, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(note, key, value)

    db.commit()
    db.refresh(note)
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return None
