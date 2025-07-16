from fastapi import FastAPI
from app.database import Base, engine
from app.routes import patient as patient_routes, visit as visit_routes

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Patient Health Records API",
    description="Backend service for managing patients, visits, vitals, and diagnoses",
    version="1.0.0"
)

# Include routers
app.include_router(patient_routes.router, prefix="/api")
app.include_router(visit_routes.router, prefix="/api")