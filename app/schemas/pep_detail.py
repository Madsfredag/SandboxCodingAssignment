from pydantic import BaseModel
from typing import Dict

class PEPDetail(BaseModel):
    id: int
    name: str
    _links: Dict[str, Dict[str, str]]
