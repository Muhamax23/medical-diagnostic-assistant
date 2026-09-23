# AI Medical Diagnostic Assistant

An early-stage FastAPI backend for a clinical decision-support prototype. The
current API provides a foundation for managing users, patients, symptoms,
diagnostic sessions, follow-up questions, medications, allergies, medical
history, vitals, and lab results.

## Project status

Phase 1: backend foundation.

The frontend, machine-learning inference, retrieval-augmented generation, and
container setup are planned but are not currently included in this repository.

## Technology

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

## Backend setup

### 1. Create and activate a virtual environment

From the repository root on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt
```

### 3. Configure the database

Copy `.env.example` to `.env` and replace the placeholder password. The
backend reads the `DATABASE_URL` environment variable.

For the current PowerShell session, you can set it directly:

```powershell
$env:DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/medical_assistant"
```

The PostgreSQL database `medical_assistant` must already exist. On startup,
the application creates tables defined by the SQLAlchemy models.

### 4. Start the API

```powershell
Set-Location backend
python -m uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

## API documentation

When the server is running, FastAPI provides interactive documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The root and health endpoints are available at `/` and `/health`.

## Repository layout

```text
backend/
  main.py                 FastAPI application entry point
  requirements.txt        Python dependencies
  app/
    database.py           SQLAlchemy engine and session configuration
    models/               Database models
    routers/              API route modules
    services/             Backend service logic
    schemas/              API schema package
.env.example              Database configuration template
```

## Safety

This project is a clinical decision-support prototype. It does not replace
qualified healthcare professionals and must not be used as an autonomous
medical diagnosis system.

Do not commit `.env` files, database passwords, patient data, or other secrets.
