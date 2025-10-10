from fastapi import APIRouter
from . import auth, content, quiz, clinics, symptoms

# Create main router
api_router = APIRouter()

# Include all routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(content.router, prefix="/content", tags=["content"])
api_router.include_router(quiz.router, prefix="/quiz", tags=["quiz"])
api_router.include_router(clinics.router, prefix="/clinics", tags=["clinics"])
api_router.include_router(symptoms.router, prefix="/symptoms", tags=["symptoms"])
