from app.database import Base, engine
from app.models.patient import Patient
from app.models.visit import Visit

# Add other models here when ready (e.g., Vitals, Diagnosis)

Base.metadata.drop_all(bind=engine)   # Optional: drops old tables
Base.metadata.create_all(bind=engine)

print("✅ Database schema recreated successfully.")
