from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.patient import PatientCreate, PatientOut
from app.models.patient import Patient
from app.database import get_db
from typing import List


router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/patients/", response_model=PatientOut)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/patients/", response_model=List[PatientOut])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()
