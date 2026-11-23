cat << 'EOF' > CHANGELOG.md
# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-11-21
### Added
- FastAPI CRUD endpoints (`POST /notes`, `GET /notes`, `PATCH /notes/{note_id}`, `DELETE /notes/{note_id}`) and upcoming reminders route (`GET /reminders/upcoming`)
- MySQL (`notes_db`) integration via SQLAlchemy and PyMySQL with URL-encoded database credentials
- Pydantic validation schemas (including `priority` pattern checks and ISO datetime handling)
- Project documentation and setup files: `README.md`, `LICENSE` (MIT), `.gitignore`, and `requirements.txt`

### Verified
- Tested note creation via Swagger UI and verified live row insertion in MySQL `notes_db.notes`
EOF

# Changelog

All notable changes to `notes-reminder-app` are documented in this file.

## [2026-11-22]

### Added
- Built full-stack Smart Notes + Reminder web application using FastAPI, SQLAlchemy, MySQL (`PyMySQL`), and HTML/JS frontend.
- Added `Note` ORM model with `id` (indexed primary key), `title`, `content` (`Text` type for long-form notes), `reminder_at`, `priority`, `tag`, `is_completed`, and `created_at`.
- Integrated `aihelper.py` to support automatic priority and tag assignment.
- Configured cloud database connectivity (`DATABASE_URL` with Aiven MySQL) and cloud hosting deployment on Render.

### Changed / Improved
- Updated UI success messages to English.
- Configured `.gitignore` to exclude secrets (`.env`), virtual environments (`.venv/`), and cache/system files (`__pycache__/`, `.DS_Store`).
- Resolved Git push/synchronization workflow issues.