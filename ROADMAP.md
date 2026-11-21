cat << 'EOF' > ROADMAP.md
# Project Roadmap

## Phase 1: Core Backend & Database (Completed)
- [x] FastAPI project setup with Pydantic validation
- [x] MySQL integration (`notes_db`) using SQLAlchemy & PyMySQL
- [x] Full CRUD endpoints (`POST`, `GET`, `PATCH`, `DELETE`)
- [x] Upcoming reminders endpoint (`GET /reminders/upcoming`)
- [x] Project documentation (`README.md`, `LICENSE`, `.gitignore`, `requirements.txt`)

## Phase 2: Web Frontend (Next)
- [ ] Enable CORS middleware in `app/main.py`
- [ ] Build clean responsive dashboard (`frontend/index.html`)
- [ ] Connect create, filter, complete, and delete actions to FastAPI endpoints
- [ ] Highlight upcoming/overdue reminders in the UI

## Phase 3: Enhancements (Planned)
- [ ] Search notes by keyword (`title` and `content`)
- [ ] Browser notifications / alert banner for due reminders
- [ ] Automated API tests with `pytest`
EOF