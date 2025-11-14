import os
import tempfile
from sqlalchemy import create_engine
from app import models, initial_data
from sqlalchemy.orm import sessionmaker

def test_db_initializes():
    db_fd, db_path = tempfile.mkstemp()
    engine = create_engine(f"sqlite:///{db_path}")
    models.Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    initial_data.populate(session)
    faqs = session.query(models.FAQ).all()
    assert any(faq.question for faq in faqs)
    os.close(db_fd)
    os.unlink(db_path)
