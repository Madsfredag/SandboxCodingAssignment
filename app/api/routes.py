from fastapi import APIRouter, Query, HTTPException
from app.services.fuzzy_match import fuzzy_match_peps
from app.db.database import SessionLocal
from app.schemas.pep import PEPMatchResponse
from app.schemas.pep_detail import PEPDetail
from app.db.crud import get_pep_by_id

router = APIRouter()

@router.get("/pep/search", response_model=PEPMatchResponse)
async def search_pep(name: str = Query(..., description="Name to search for")):
    return fuzzy_match_peps(name)

@router.get("/pep/{pep_id}", response_model=PEPDetail)
async def get_pep(pep_id: int):
    db = SessionLocal()
    pep = get_pep_by_id(db, pep_id)
    db.close()
    if not pep:
        raise HTTPException(status_code=404, detail="PEP not found")

    return {
    "id": pep.id,
    "name": pep.name,
    "birth_date": pep.birth_date,
    "added_date": pep.added_date,
    "_links": {"self": {"href": f"/pep/{pep.id}"}}
    }

@router.get("/pep/all")
async def get_all_peps():
    from app.db.database import SessionLocal
    from app.db.models import PEP
    db = SessionLocal()
    peps = db.query(PEP).all()
    db.close()
    return [pep.name for pep in peps]
