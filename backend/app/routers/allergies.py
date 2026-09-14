from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.allergy import Allergy

router = APIRouter(
    prefix="/patients",
    tags=["Allergies"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{patient_id}/allergies")
def add_allergy(
    patient_id: int,
    allergen: str,
    reaction: str = None,
    severity: str = None,
    db: Session = Depends(get_db)
):
    allergy = Allergy(
        patient_id=patient_id,
        allergen=allergen,
        reaction=reaction,
        severity=severity
    )

    db.add(allergy)
    db.commit()
    db.refresh(allergy)

    return allergy


@router.get("/{patient_id}/allergies")
def get_allergies(
    patient_id: int,
    db: Session = Depends(get_db)
):
    results = (
        db.query(Allergy)
        .filter(Allergy.patient_id == patient_id)
        .all()
    )

    return results