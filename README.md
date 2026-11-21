cat << 'EOF' > README.md
# Smart Notes + Reminder API

A backend web application built with **FastAPI**, **SQLAlchemy**, **PyMySQL**, and **MySQL** to create, list, filter, update, and delete notes with optional reminders and automatic priority/tag inference.

## Tech Stack

- **Framework:** FastAPI + Uvicorn
- **ORM & Database:** SQLAlchemy + PyMySQL + MySQL (`notes_db`)
- **Configuration:** python-dotenv (`.env`)
- **Validation:** Pydantic

## Project Structure

```text
notes-reminder-app/
├── app/
│   ├── __init__.py
│   ├── ai_helper.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .env
└── README.md