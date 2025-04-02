from pydantic import BaseModel

class ProblemDetail(BaseModel):
    type: str = "about:blank"
    title: str
    status: int
    detail: str
