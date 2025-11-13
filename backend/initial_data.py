from sqlalchemy.orm import Session
from app.models.models import STIInformation, QuizQuestion, Clinic, Symptom, FAQ, ContentResource
from app.config.database import SessionLocal, Base, engine
import json

print("Database file in use:", engine.url.database)


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

        faqs_data = [
            {"question": "What is sexual consent?", "answer": "Consent is a clear and voluntary agreement to participate in sexual activity."},
            {"question": "Where can I get tested for STIs in Nairobi?", "answer": "Check the clinic locator on our site or visit LVCT Health clinics in Nairobi."},
            {"question": "Can I get an STI from a public toilet?", "answer": "STIs are not spread through toilet seats. They typically spread via sexual contact."},
            {"question": "What are common symptoms of STIs?", "answer": "Symptoms can include sores, pain when urinating, discharge, or none at all."},
            {"question": "Can birth control pills prevent STIs?", "answer": "No. Birth control pills prevent pregnancy, not infections. Use condoms for STI protection."},
            {"question": "How do I talk to my partner about STIs?", "answer": "Be honest, open, and respectful. Share facts and concerns early on."},
            {"question": "Is HIV curable?", "answer": "HIV is not curable, but with medication, people can live healthy lives."},
            {"question": "What should I do after unprotected sex?", "answer": "Consider STI testing and emergency contraception. Talk to a healthcare provider."},
            {"question": "Do condoms protect against all STIs?", "answer": "They protect against most, but not all. Regular testing is important."},
            {"question": "Where can I get emergency contraception?", "answer": "Most pharmacies, hospitals, and clinics will help you find emergency contraception."},
            {"question": "Can I refuse sex after saying yes?", "answer": "Yes. Consent can be withdrawn at any point."},
            {"question": "Can STIs show no symptoms?", "answer": "Yes. Many STIs can be silent for months or years."},
            {"question": "Who can help me after sexual assault?", "answer": "Reach out to clinics, university counseling or hotlines like Kenya 1195."},
            {"question": "Should I get vaccinated for HPV?", "answer": "Yes, vaccination prevents HPV infections and reduces cancer risk."},
            {"question": "How often should I get tested for STIs?", "answer": "If sexually active, testing every six months is a safe rule."}
        ]
        for faq in faqs_data:
            db_faq = FAQ(**faq)
            db.add(db_faq)
    
        
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
