from app import models

def test_create_faq_model():
    faq = models.FAQ(question="Sample Q?", answer="Sample A.")
    assert faq.question == "Sample Q?"
    assert faq.answer == "Sample A."
