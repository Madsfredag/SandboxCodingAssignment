from typing import List, Dict
from pydantic import BaseModel

class PEPMatch(BaseModel):
    name: str
    score: float
    _links: Dict[str, Dict[str, str]]

class PEPMatchResponse(BaseModel):
    _links: Dict[str, Dict[str, str]]
    matches: List[PEPMatch]
