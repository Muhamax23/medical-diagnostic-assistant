from fastapi import FastAPI

from app.database import engine, Base
from app.models import (
    User,
    Patient,
    Symptom,
    PatientSymptom,
    MedicalHistory,
    Medication,
    Allergy,
    DiagnosticSession,
    Vitals,
    LabResult,
    AIAssessment,
    Diagnosis,
    SessionDiagnosis,
    FollowUpQuestion
    )

from app.routers import patients, users, symptoms, patient_symptoms, diagnostic_sessions, vitals, lab_results, medical_history, medications, allergies, follow_up_questions #, diagnostic_sessions, ai_assessments, diagnoses, session_diagnoses

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Medical Diagnostic Assistant",
    description="Clinical decision-support system for medical information and diagnostic assistance.",
    version="0.1.0"
)


app.include_router(patients.router)
app.include_router(users.router)
app.include_router(symptoms.router)
app.include_router(patient_symptoms.router)
app.include_router(diagnostic_sessions.router)
app.include_router(vitals.router)
app.include_router(lab_results.router)
app.include_router(medical_history.router)
app.include_router(medications.router)
app.include_router(allergies.router)
app.include_router(follow_up_questions.router)


@app.get("/")
def root():
    return {
        "message": "AI Medical Diagnostic Assistant API is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

