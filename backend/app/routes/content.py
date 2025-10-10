from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..models.models import STIInformation
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class STIBase(BaseModel):
    name: str
    description: str
    symptoms: str
    prevention: str
    treatment: str

class STICreate(STIBase):
    pass

class STI(STIBase):
    id: int

    class Config:
        from_attributes = True

@router.get("/", response_model=List[STI])
def get_all_sti_info(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(STIInformation).offset(skip).limit(limit).all()

@router.post("/", response_model=STI)
def create_sti_info(sti: STICreate, db: Session = Depends(get_db)):
    db_sti = STIInformation(**sti.dict())
    db.add(db_sti)
    db.commit()
    db.refresh(db_sti)
    return db_sti

@router.get("/{sti_id}", response_model=STI)
def get_sti_info(sti_id: int, db: Session = Depends(get_db)):
    sti = db.query(STIInformation).filter(STIInformation.id == sti_id).first()
    if not sti:
        raise HTTPException(status_code=404, detail="STI information not found")
    return sti

@router.put("/{sti_id}", response_model=STI)
def update_sti_info(sti_id: int, sti: STICreate, db: Session = Depends(get_db)):
    db_sti = db.query(STIInformation).filter(STIInformation.id == sti_id).first()
    if not db_sti:
        raise HTTPException(status_code=404, detail="STI information not found")
    
    for key, value in sti.dict().items():
        setattr(db_sti, key, value)
    
    db.commit()
    db.refresh(db_sti)
    return db_sti

@router.delete("/{sti_id}")
def delete_sti_info(sti_id: int, db: Session = Depends(get_db)):
    db_sti = db.query(STIInformation).filter(STIInformation.id == sti_id).first()
    if not db_sti:
        raise HTTPException(status_code=404, detail="STI information not found")
    
    db.delete(db_sti)
    db.commit()
    return {"message": "STI information deleted"}
