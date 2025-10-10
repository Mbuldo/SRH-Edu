from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, content, quiz, clinics, symptoms
from app.config.database import engine
from app.models import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Healthy Sex, Healthy Life API",
    description="API for STI awareness and education platform",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"  # Remove this in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(content.router, prefix="/api/content", tags=["Content"])
app.include_router(quiz.router, prefix="/api/quiz", tags=["Quiz"])
app.include_router(clinics.router, prefix="/api/clinics", tags=["Clinics"])
app.include_router(symptoms.router, prefix="/api/symptoms", tags=["Symptoms"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Healthy Sex, Healthy Life API",
        "docs": "/docs",
        "version": "1.0.0"
    }
