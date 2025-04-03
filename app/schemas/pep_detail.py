from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import date

class PEPDetail(BaseModel):
    id: int
    name: str
    birth_date: Optional[date]
    added_date: Optional[date]
    links: Dict[str, Dict[str, str]] = Field(..., alias="_links")

    class Config:
        populate_by_name = True
