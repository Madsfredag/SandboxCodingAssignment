from fastapi import APIRouter, Query
from app.services.fuzzy_match import fuzzy_match_peps
from app.schemas.pep import PEPMatchResponse

router = APIRouter()

@router.get("/pep/search", response_model=PEPMatchResponse)
async def search_pep(name: str = Query(..., description="Name to search for")):
    return fuzzy_match_peps(name)

@router.get("/pep/all")
async def get_all_peps():
    from app.db.database import SessionLocal
    from app.db.models import PEP
    db = SessionLocal()
    peps = db.query(PEP).all()
    db.close()
    return [pep.name for pep in peps]
