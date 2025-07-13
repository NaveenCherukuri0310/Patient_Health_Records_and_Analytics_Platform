from pydantic import BaseModel
from datetime import date


class VisitBase(BaseModel):
    patient_id: int
    visit_date: date
    doctor_name: str
    specialization: str
    reason: str

class VisitCreate(VisitBase):
    pass

class VisitOut(VisitBase):
    visit_id: int

    class Config:
        from_attributes = True

