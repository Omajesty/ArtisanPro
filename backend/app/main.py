from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlmodel import Session

from app.core.database import get_session

app = FastAPI(title="ArtisanPro API")


@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/v1/health/db")
def database_health_check(session: Annotated[Session, Depends(get_session)]):
    session.execute(text("SELECT 1"))
    return {"database": "ok"}
