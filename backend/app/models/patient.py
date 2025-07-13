from sqlalchemy import Column, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    email_id = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    
    visits = relationship("Visit", back_populates="patient")
