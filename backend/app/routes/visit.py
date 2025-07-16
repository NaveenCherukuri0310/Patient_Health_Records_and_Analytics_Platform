from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.visit import Visit
from app.schemas.visit import VisitCreate, VisitOut
from app.database import get_db
from typing import List

router = APIRouter(prefix="/visits", tags=["Visits"])


@router.post("/visits/", response_model=VisitOut)
def create_visit(visit: VisitCreate, db: Session = Depends(get_db)):
    db_visit = Visit(**visit.dict())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit

@router.get("/visits/", response_model=List[VisitOut])
def get_visits(db: Session = Depends(get_db)):
    return db.query(Visit).all()
