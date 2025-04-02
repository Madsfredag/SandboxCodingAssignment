from sqlalchemy.orm import Session
from app.db.models import PEP

def get_pep_by_id(db: Session, pep_id: int):
    return db.query(PEP).filter(PEP.id == pep_id).first()
