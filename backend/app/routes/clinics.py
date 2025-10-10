from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..models.models import Clinic
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

class ClinicBase(BaseModel):
    name: str
    area: str
    address: str
    contact: str
    operating_hours: str
    services: List[str]
    is_active: bool = True

class ClinicCreate(ClinicBase):
    pass

class ClinicResponse(ClinicBase):
    id: int

    class Config:
        from_attributes = True

@router.get("/", response_model=List[ClinicResponse])
def get_clinics(
    area: Optional[str] = None,
    is_active: bool = True,
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(Clinic)
    if area:
        query = query.filter(Clinic.area == area)
    if is_active is not None:
        query = query.filter(Clinic.is_active == is_active)
    
    clinics = query.offset(skip).limit(limit).all()
    for clinic in clinics:
        clinic.services = json.loads(clinic.services)
    return clinics

@router.post("/", response_model=ClinicResponse)
def create_clinic(clinic: ClinicCreate, db: Session = Depends(get_db)):
    db_clinic = Clinic(
        name=clinic.name,
        area=clinic.area,
        address=clinic.address,
        contact=clinic.contact,
        operating_hours=clinic.operating_hours,
        services=json.dumps(clinic.services),
        is_active=clinic.is_active
    )
    db.add(db_clinic)
    db.commit()
    db.refresh(db_clinic)
    db_clinic.services = json.loads(db_clinic.services)
    return db_clinic

@router.get("/{clinic_id}", response_model=ClinicResponse)
def get_clinic(clinic_id: int, db: Session = Depends(get_db)):
    clinic = db.query(Clinic).filter(Clinic.id == clinic_id).first()
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    clinic.services = json.loads(clinic.services)
    return clinic

@router.put("/{clinic_id}", response_model=ClinicResponse)
def update_clinic(clinic_id: int, clinic_update: ClinicCreate, db: Session = Depends(get_db)):
    db_clinic = db.query(Clinic).filter(Clinic.id == clinic_id).first()
    if not db_clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    
    update_data = clinic_update.dict()
    update_data["services"] = json.dumps(update_data["services"])
    
    for key, value in update_data.items():
        setattr(db_clinic, key, value)
    
    db.commit()
    db.refresh(db_clinic)
    db_clinic.services = json.loads(db_clinic.services)
    return db_clinic

@router.delete("/{clinic_id}")
def delete_clinic(clinic_id: int, db: Session = Depends(get_db)):
    clinic = db.query(Clinic).filter(Clinic.id == clinic_id).first()
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    
    clinic.is_active = False
    db.commit()
    return {"message": "Clinic deactivated"}
