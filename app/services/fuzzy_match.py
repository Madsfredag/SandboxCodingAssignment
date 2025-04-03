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
    print("Total PEPs in DB:", len(all_peps))

    for pep in all_peps:
        score = fuzz.partial_ratio(query.lower(), pep.name.lower())
        logging.info(f"Match '{query}' vs '{pep.name}' → score: {score}")
        if score >= 50:
            results.append(PEPMatch(
                name=pep.name,
                score=score,
                links={"self": {"href": f"/pep/{pep.id}"}}
            ))

    db.close()

    top_matches = sorted(results, key=lambda r: r.score, reverse=True)[:10]
    print("Returning matches:", top_matches)
    return PEPMatchResponse(
        links={"self": {"href": f"/pep/search?name={query}"}},
        matches=top_matches
    )
