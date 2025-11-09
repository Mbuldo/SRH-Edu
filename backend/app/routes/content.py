from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..models.models import STIInformation, FAQ, HealthTip
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

# Combined FAQ CRUD
@router.post("/faqs/")
def create_faq(question: str, answer: str, db: Session = Depends(get_db)):
    faq = FAQ(question=question, answer=answer)
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq

@router.get("/faqs/")
def read_faqs(db: Session = Depends(get_db)):
    return db.query(FAQ).all()

@router.get("/faqs/{faq_id}")
def read_faq(faq_id: int, db: Session = Depends(get_db)):
    faq = db.query(FAQ).get(faq_id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return faq

@router.put("/faqs/{faq_id}")
def update_faq(faq_id: int, question: str, answer: str, db: Session = Depends(get_db)):
    faq = db.query(FAQ).get(faq_id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    faq.question = question
    faq.answer = answer
    db.commit()
    return faq

@router.delete("/faqs/{faq_id}")
def delete_faq(faq_id: int, db: Session = Depends(get_db)):
    faq = db.query(FAQ).get(faq_id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    db.delete(faq)
    db.commit()
    return {"ok": True}

# Combined HealthTip CRUD
@router.post("/healthtips/")
def create_tip(tip: str, created_by: str, db: Session = Depends(get_db)):
    health_tip = HealthTip(tip=tip, created_by=created_by)
    db.add(health_tip)
    db.commit()
    db.refresh(health_tip)
    return health_tip

@router.get("/healthtips/")
def get_tips(db: Session = Depends(get_db)):
    return db.query(HealthTip).all()

@router.get("/healthtips/{tip_id}")
def get_tip(tip_id: int, db: Session = Depends(get_db)):
    tip = db.query(HealthTip).get(tip_id)
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")
    return tip

@router.put("/healthtips/{tip_id}")
def update_tip(tip_id: int, tip: str, db: Session = Depends(get_db)):
    tip_obj = db.query(HealthTip).get(tip_id)
    if not tip_obj:
        raise HTTPException(status_code=404, detail="Tip not found")
    tip_obj.tip = tip
    db.commit()
    return tip_obj

@router.delete("/healthtips/{tip_id}")
def delete_tip(tip_id: int, db: Session = Depends(get_db)):
    tip_obj = db.query(HealthTip).get(tip_id)
    if not tip_obj:
        raise HTTPException(status_code=404, detail="Tip not found")
    db.delete(tip_obj)
    db.commit()
    return {"ok": True}
