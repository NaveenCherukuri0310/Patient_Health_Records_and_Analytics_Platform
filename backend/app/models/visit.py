from sqlalchemy import Column, String, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Visit(Base):
    __tablename__ = "visits"

    visit_id = Column(String, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"), nullable=False)
    visit_date = Column(Date, nullable=False)
    doctor_name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    reason = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="visits")