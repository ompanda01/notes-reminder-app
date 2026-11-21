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