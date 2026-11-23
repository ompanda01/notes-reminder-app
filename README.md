# Smart Notes + Reminder API

A full-stack notes and reminder web application built with **FastAPI**, **SQLAlchemy**, **PyMySQL**, **MySQL**, and a web frontend to create, list, filter, pin, update, and delete notes with optional reminders and automatic priority/tag inference.

## Features

- Create, read, update, and delete notes with optional reminder timestamps
- Pin and unpin notes (`is_pinned`) with pinned notes sorted to the top
- Filter notes by view/status, priority, and tag, plus live search
- Interactive Cadence web UI (`frontend/index.html`) with dark/light theme and markdown preview

## Tech Stack

- **Framework:** FastAPI + Uvicorn
- **ORM & Database:** SQLAlchemy + PyMySQL + MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Configuration:** python-dotenv (`.env`)
- **Validation:** Pydantic

## Project Structure

notes-reminder-app/
├── app/
│   ├── __init__.py
│   ├── ai_helper.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── frontend/
│   └── index.html
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── ROADMAP.md

## Run Locally

```bash
uvicorn app.main:app --reload

