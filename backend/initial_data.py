from sqlalchemy.orm import Session
from app.models.models import STIInformation, QuizQuestion, Clinic, Symptom
from app.config.database import SessionLocal
import json

def init_db():
    db = SessionLocal()
    try:
        # Add STI Information
        sti_data = [
            {
                "name": "HIV/AIDS",
                "description": "HIV (Human Immunodeficiency Virus) is a virus that attacks the immune system.",
                "symptoms": "Early symptoms may include fever, chills, rash, night sweats, muscle aches, fatigue.",
                "prevention": "Use protection during sex, avoid sharing needles, get tested regularly.",
                "treatment": "Antiretroviral therapy (ART) can help manage HIV effectively."
            },
            {
                "name": "Chlamydia",
                "description": "A common bacterial infection that can be easily treated.",
                "symptoms": "Many people have no symptoms. May include discharge, burning sensation.",
                "prevention": "Use protection during sex, regular testing.",
                "treatment": "Treated with antibiotics."
            },
            {
                "name": "Gonorrhea",
                "description": "A bacterial infection that can cause serious complications if untreated.",
                "symptoms": "Discharge, pain during urination, swollen genitals.",
                "prevention": "Use protection, regular testing, monogamous relationships.",
                "treatment": "Treated with specific antibiotics."
            }
        ]

        for sti in sti_data:
            db_sti = STIInformation(**sti)
            db.add(db_sti)

        # Add Quiz Questions
        quiz_data = [
            {
                "question": "Which of the following is NOT a common way STIs are transmitted?",
                "options": json.dumps(["Sharing food", "Unprotected sex", "Blood contact", "Mother to child"]),
                "correct_answer": 0,
                "explanation": "STIs are not transmitted through sharing food or drinks."
            },
            {
                "question": "What percentage of STIs show no immediate symptoms?",
                "options": json.dumps(["25%", "50%", "75%", "100%"]),
                "correct_answer": 2,
                "explanation": "Approximately 75% of STIs may not show immediate symptoms."
            }
        ]

        for question in quiz_data:
            db_question = QuizQuestion(**question)
            db.add(db_question)

        # Add Clinics
        clinic_data = [
            {
                "name": "Nairobi STI Care Center",
                "area": "CBD",
                "address": "Kenyatta Avenue",
                "contact": "+254 20 XXX XXXX",
                "operating_hours": "Mon-Fri: 8am-6pm",
                "services": json.dumps(["Testing", "Treatment", "Counseling"]),
                "is_active": True
            },
            {
                "name": "Westlands Health Center",
                "area": "Westlands",
                "address": "Waiyaki Way",
                "contact": "+254 20 XXX XXXX",
                "operating_hours": "24/7",
                "services": json.dumps(["Testing", "Emergency Care"]),
                "is_active": True
            }
        ]

        for clinic in clinic_data:
            db_clinic = Clinic(**clinic)
            db.add(db_clinic)

        # Add Symptoms
        symptom_data = [
            {
                "name": "Unusual discharge",
                "description": "Abnormal fluid from genitals",
                "related_conditions": json.dumps(["Chlamydia", "Gonorrhea"]),
                "severity_level": 2,
                "seek_care": True
            },
            {
                "name": "Burning urination",
                "description": "Pain or burning sensation during urination",
                "related_conditions": json.dumps(["UTI", "Chlamydia", "Gonorrhea"]),
                "severity_level": 2,
                "seek_care": True
            }
        ]

        for symptom in symptom_data:
            db_symptom = Symptom(**symptom)
            db.add(db_symptom)

        db.commit()
        print("Database initialized with sample data!")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Creating initial data...")
    init_db()
