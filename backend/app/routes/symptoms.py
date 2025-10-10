from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..models.models import Symptom
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

class SymptomBase(BaseModel):
    name: str
    description: str
    related_conditions: List[str]
    severity_level: int
    seek_care: bool = False

class SymptomCreate(SymptomBase):
    pass

class SymptomResponse(SymptomBase):
    id: int

    class Config:
        from_attributes = True

@router.get("/", response_model=List[SymptomResponse])
def get_symptoms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    symptoms = db.query(Symptom).offset(skip).limit(limit).all()
    for symptom in symptoms:
        symptom.related_conditions = json.loads(symptom.related_conditions)
    return symptoms

@router.post("/", response_model=SymptomResponse)
def create_symptom(symptom: SymptomCreate, db: Session = Depends(get_db)):
    db_symptom = Symptom(
        name=symptom.name,
        description=symptom.description,
        related_conditions=json.dumps(symptom.related_conditions),
        severity_level=symptom.severity_level,
        seek_care=symptom.seek_care
    )
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)
    db_symptom.related_conditions = json.loads(db_symptom.related_conditions)
    return db_symptom

@router.post("/check")
def check_symptoms(symptoms: List[str], db: Session = Depends(get_db)):
    results = []
    should_seek_care = False
    max_severity = 0
    
    for symptom_name in symptoms:
        symptom = db.query(Symptom).filter(Symptom.name == symptom_name).first()
        if symptom:
            results.append({
                "symptom": symptom.name,
                "severity": symptom.severity_level,
                "seek_care": symptom.seek_care,
                "description": symptom.description,
                "related_conditions": json.loads(symptom.related_conditions)
            })
            should_seek_care = should_seek_care or symptom.seek_care
            max_severity = max(max_severity, symptom.severity_level)
    
    return {
        "results": results,
        "seek_care": should_seek_care,
        "severity_level": max_severity,
        "recommendation": "Please seek immediate medical attention" if should_seek_care 
                         else "Monitor your symptoms and consult a healthcare provider if they persist"
    }

@router.get("/{symptom_id}", response_model=SymptomResponse)
def get_symptom(symptom_id: int, db: Session = Depends(get_db)):
    symptom = db.query(Symptom).filter(Symptom.id == symptom_id).first()
    if not symptom:
        raise HTTPException(status_code=404, detail="Symptom not found")
    symptom.related_conditions = json.loads(symptom.related_conditions)
    return symptom
