# ✅ FastAPI Task Management API

A portfolio-ready task management REST API built with FastAPI and PostgreSQL.

## Features
- JWT authentication
- User registration/login
- Create, read, update and delete tasks
- Task priorities: low, medium, high
- Task statuses: pending, in_progress, completed, cancelled
- Due dates
- Task filtering
- Quick complete endpoint
- Task statistics dashboard
- PostgreSQL + SQLAlchemy
- Swagger/OpenAPI
- Docker + Docker Compose
- Pytest

## Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger: http://127.0.0.1:8000/docs

## Docker
```bash
docker compose up --build
```

## Main endpoints
- POST `/auth/register`
- POST `/auth/login`
- POST `/tasks/`
- GET `/tasks/`
- GET `/tasks/{id}`
- PUT `/tasks/{id}`
- PATCH `/tasks/{id}/complete`
- DELETE `/tasks/{id}`
- GET `/tasks/summary/stats`

## GitHub
Repository: `fastapi-task-management-api`

Description: `Task management REST API built with FastAPI, PostgreSQL, JWT authentication and SQLAlchemy.`

## Author
Akshay Borase
