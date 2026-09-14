from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.diagnostic_session import DiagnosticSession

router = APIRouter(
    prefix="/diagnostic-sessions",
    tags=["Diagnostic Sessions"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_diagnostic_session(
    patient_id: int,
    db: Session = Depends(get_db)
):
    session = DiagnosticSession(
        patient_id=patient_id,
        status="active"
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session