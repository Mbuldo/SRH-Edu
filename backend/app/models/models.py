from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from ..config.database import Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class STIInformation(Base):
    __tablename__ = "sti_information"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    symptoms = Column(Text)
    prevention = Column(Text)
    treatment = Column(Text)

class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    options = Column(String)  # Stored as JSON string
    correct_answer = Column(Integer)
    explanation = Column(Text)

class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    area = Column(String)
    address = Column(String)
    contact = Column(String)
    operating_hours = Column(String)
    services = Column(String)  # Stored as JSON string
    is_active = Column(Boolean, default=True)

class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    related_conditions = Column(String)  # Stored as JSON string
    severity_level = Column(Integer)
    seek_care = Column(Boolean, default=False)
