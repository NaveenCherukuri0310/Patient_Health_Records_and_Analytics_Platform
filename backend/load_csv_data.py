import csv
from datetime import datetime
from app.database import SessionLocal
from app.models.patient import Patient
from app.models.visit import Visit

# Create DB session
session = SessionLocal()

# Track existing emails to avoid duplicates
existing_emails = {p.email_id for p in session.query(Patient.email_id).all()}

# Load Patients
with open("data/patients.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Email Id"] in existing_emails:
            continue  # Skip duplicates

        patient = Patient(
            full_name=row["Full Name"],
            date_of_birth=datetime.strptime(row["Date of Birth"], "%Y-%m-%d").date(),
            gender=row["Gender"],
            email_id=row["Email Id"],
            phone_number=row["Phone Number"]
        )
        session.add(patient)
        existing_emails.add(row["Email Id"])  # Add to tracking set

# Load Visits
with open("data/visits.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        visit = Visit(
            visit_id=row["Visit ID"],  # Keep as string
            patient_id=int(row["Patient ID"]),
            visit_date=datetime.strptime(row["Visit Date"], "%Y-%m-%d").date(),
            doctor_name=row["Doctor Name"],
            specialization=row["Specialization"],
            reason=row["Reason"]
        )
        session.add(visit)

# Commit all at once
session.commit()
session.close()

print("✅ Data loaded successfully.")
