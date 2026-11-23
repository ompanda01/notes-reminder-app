cat << 'EOF' > ROADMAP.md
# Project Roadmap

## Phase 1: Core Backend & Database (Completed)
- [x] FastAPI project setup with Pydantic validation
- [x] MySQL integration (`notes_db`) using SQLAlchemy & PyMySQL
- [x] Full CRUD endpoints (`POST`, `GET`, `PATCH`, `DELETE`)
- [x] Upcoming reminders endpoint (`GET /reminders/upcoming`)
- [x] Project documentation (`README.md`, `LICENSE`, `.gitignore`, `requirements.txt`)

## Phase 2: Web Frontend (Next)
- [x] Enable CORS middleware in `app/main.py`
- [x] Build clean responsive dashboard (`frontend/index.html`)
- [x] Connect create, filter, complete, and delete actions to FastAPI endpoints
- [ ] Highlight upcoming/overdue reminders in the UI

## Phase 3: Enhancements (Planned)
- [x] Search notes by keyword (`title` and `content`)
- [ ] Browser notifications / alert banner for due reminders
- [x] Pin/unpin notes (`is_pinned`) with MySQL persistence and top sorting
- [ ] Automated API tests with `pytest`
EOF