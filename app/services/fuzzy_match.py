from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import PEP
from app.schemas.pep import PEPMatchResponse, PEPMatch
from rapidfuzz import fuzz
import logging

def fuzzy_match_peps(query: str) -> PEPMatchResponse:
    db: Session = SessionLocal()
    all_peps = db.query(PEP).all()
    results = []

    for pep in all_peps:
        score = fuzz.ratio(query.lower(), pep.name.lower())
        logging.info(f"Match '{query}' vs '{pep.name}' → score: {score}")
        if score >= 40:  # lowered threshold
            results.append(PEPMatch(
                name=pep.name,
                score=score,
                _links={"self": {"href": f"/pep/search?name={pep.name}"}}
            ))

    db.close()

    return PEPMatchResponse(
        _links={"self": {"href": f"/pep/search?name={query}"}},
        matches=sorted(results, key=lambda r: r.score, reverse=True)
    )
