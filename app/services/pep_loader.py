from app.db.database import SessionLocal
from app.db.models import PEP

def load_peps():
    db = SessionLocal()

    existing = db.query(PEP).count()
    if existing == 0:
        peps = ["Mette Frederiksen", "Lars Løkke Rasmussen", "Inger Støjberg"]
        for name in peps:
            db.add(PEP(name=name))
        db.commit()

    db.close()
