from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.api.routes import router
from app.core.config import setup_logging
from app.db.database import init_db
from app.services.pep_loader import load_peps_from_excel
from app.schemas.error import ProblemDetail

app = FastAPI(
    title="PEP Checker API",
    version="1.0.0"
)

app.include_router(router)
setup_logging()

@app.on_event("startup")
def startup():
    init_db()
    load_peps_from_excel()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ProblemDetail(
            title=exc.detail,
            status=exc.status_code,
            detail=exc.detail
        ).dict()
    )
