from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.models import ContentResource
from ..config.database import get_db
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ContentResourceBase(BaseModel):
    title: str
    body: str
    url: str
    category: str

class ContentResourceCreate(ContentResourceBase):
    pass

class ContentResourceOut(ContentResourceBase):
    id: int
    class Config:
        from_attributes = True

@router.post("/resources/", response_model=ContentResourceOut)
def create_resource(resource: ContentResourceCreate, db: Session = Depends(get_db)):
    db_resource = ContentResource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@router.get("/resources/", response_model=List[ContentResourceOut])
def list_resources(db: Session = Depends(get_db)):
    return db.query(ContentResource).all()

@router.get("/resources/{resource_id}", response_model=ContentResourceOut)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    res = db.query(ContentResource).get(resource_id)
    if not res:
        raise HTTPException(status_code=404, detail="Resource not found")
    return res

@router.put("/resources/{resource_id}", response_model=ContentResourceOut)
def update_resource(resource_id: int, resource: ContentResourceCreate, db: Session = Depends(get_db)):
    db_resource = db.query(ContentResource).get(resource_id)
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    for key, value in resource.dict().items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@router.delete("/resources/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = db.query(ContentResource).get(resource_id)
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return {"ok": True}
