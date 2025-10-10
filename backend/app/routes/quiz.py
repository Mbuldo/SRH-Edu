from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..models.models import QuizQuestion
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

class QuestionBase(BaseModel):
    question: str
    options: List[str]
    correct_answer: int
    explanation: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int

    class Config:
        from_attributes = True

@router.get("/questions", response_model=List[Question])
def get_questions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    questions = db.query(QuizQuestion).offset(skip).limit(limit).all()
    # Convert JSON string to list for options
    for q in questions:
        q.options = json.loads(q.options)
    return questions

@router.post("/questions", response_model=Question)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = QuizQuestion(
        question=question.question,
        options=json.dumps(question.options),
        correct_answer=question.correct_answer,
        explanation=question.explanation
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    db_question.options = json.loads(db_question.options)
    return db_question

@router.put("/questions/{question_id}", response_model=Question)
def update_question(question_id: int, question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = db.query(QuizQuestion).filter(QuizQuestion.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db_question.question = question.question
    db_question.options = json.dumps(question.options)
    db_question.correct_answer = question.correct_answer
    db_question.explanation = question.explanation
    
    db.commit()
    db.refresh(db_question)
    db_question.options = json.loads(db_question.options)
    return db_question

@router.delete("/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    db_question = db.query(QuizQuestion).filter(QuizQuestion.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db.delete(db_question)
    db.commit()
    return {"message": "Question deleted"}

@router.post("/submit")
def submit_quiz(answers: dict, db: Session = Depends(get_db)):
    score = 0
    results = []
    
    for question_id, answer in answers.items():
        question = db.query(QuizQuestion).filter(QuizQuestion.id == int(question_id)).first()
        if question and answer == question.correct_answer:
            score += 1
        results.append({
            "question_id": question_id,
            "correct": question and answer == question.correct_answer,
            "explanation": question.explanation if question else None
        })
    
    return {
        "score": score,
        "total": len(answers),
        "percentage": (score / len(answers)) * 100 if answers else 0,
        "results": results
    }
