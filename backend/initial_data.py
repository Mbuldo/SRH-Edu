from sqlalchemy.orm import Session
from app.models.models import STIInformation, QuizQuestion, Clinic, Symptom, FAQ, ContentResource
from app.config.database import SessionLocal, Base, engine
import json

Base.metadata.create_all(bind=engine)


def init_db():
    db = SessionLocal()
    try:
        resources_data = [
            {
                "title": "RAINN - What is Consent?",
                "body": "Comprehensive guide on sexual consent, communication, boundaries, and safety.",
                "url": "https://www.rainn.org/articles/what-is-consent",
                "category": "consent"
            },
            {
                "title": "CDC - STI Prevention",
                "body": "Official US CDC information on STI prevention, safe sex, and regular testing.",
                "url": "https://www.cdc.gov/std/prevention/default.htm",
                "category": "sti-prevention"
            },
            {
                "title": "LVCT Health Kenya Clinic Locator",
                "body": "Find STI testing and counseling clinics in Nairobi and Kenya.",
                "url": "https://lvcthealth.org/clinic-locator/",
                "category": "clinic-locator"
            },
            {
                "title": "Kenya National Sexual Violence Helpline",
                "body": "Call 1195 for help after assault. More resources at RSV Awareness Kenya.",
                "url": "https://www.rsvawarenesskenya.org/get-help",
                "category": "support"
            },
            {
                "title": "WHO Sexual Health Toolkit",
                "body": "Global advice on sexual health, respectful relationships, and legal rights.",
                "url": "https://www.who.int/teams/sexual-and-reproductive-health-and-research/sexual-health",
                "category": "general-health"
            },
            {
                "title": "University of Nairobi Counseling Center",
                "body": "Support services for students: sexual health, safe relationships, and mental health.",
                "url": "https://studentlife.uonbi.ac.ke/node/25",
                "category": "student-support"
            }
        ]

        for res in resources_data:
            db_res = ContentResource(**res)
            db.add(db_res)
        
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
