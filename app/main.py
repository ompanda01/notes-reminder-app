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