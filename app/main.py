from fastapi import FastAPI
from app.api.routes import router
from app.core.config import setup_logging
from app.db.database import init_db
from app.services.pep_loader import load_peps_from_excel

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
