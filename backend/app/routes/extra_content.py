from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.models import FAQ, HealthTip
from ..config.database import get_db

router = APIRouter()

# FAQ CRUD
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

# HealthTip CRUD
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
