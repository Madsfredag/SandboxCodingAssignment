from typing import List, Dict
from pydantic import BaseModel, Field

class PEPMatch(BaseModel):
    name: str
    score: float
    links: Dict[str, Dict[str, str]] = Field(..., alias="_links")

    class Config:
        populate_by_name = True
        json_encoders = {
            Dict: lambda v: v  # ensures dicts are preserved as-is
        }

class PEPMatchResponse(BaseModel):
    links: Dict[str, Dict[str, str]] = Field(..., alias="_links")
    matches: list[PEPMatch]

    class Config:
        populate_by_name = True
