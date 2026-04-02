from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from app.core.db import init_db, get_session
from app.models.industrial import IndustrialClient

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/clients")
def read_clients(session: Session = Depends(get_session)):
    clients = session.exec(select(IndustrialClient)).all()
    return clients

