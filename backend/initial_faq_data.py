from backend.app.models.models import FAQ, HealthTip
from backend.app.config.database import SessionLocal

def seed_faqs():
    db = SessionLocal()
    faqs = [
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
    for f in faqs:
        faq = FAQ(**f)
        db.add(faq)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_faqs()
