from pydantic import BaseModel, EmailStr
from datetime import date

class PatientBase(BaseModel):
    full_name: str
    date_of_birth: date
    gender: str
    email_id: str
    phone_number: str

class PatientCreate(PatientBase):
    pass

class PatientOut(PatientBase):
    patient_id: int

    class Config:
        from_attributes = True
