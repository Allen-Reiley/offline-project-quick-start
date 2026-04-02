from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import List

from app.core.db import engine, init_db, get_session
from app.models.industrial import IndustrialClient

app = FastAPI(title="AuraWorks Master Seed - Industrial Engine")

# CORS Setup: Essential for the Frontend to talk to the Backend locally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    # This creates the aura_local.db and tables if they don't exist
    init_db()

@app.get("/")
def read_root():
    return {"status": "AuraWorks Engine Online", "location": "East Rand, Gauteng"}

# --- Industrial Lead Routes ---

@app.post("/clients/", response_model=IndustrialClient)
def create_client(client: IndustrialClient, session: Session = Depends(get_session)):
    session.add(client)
    session.commit()
    session.refresh(client)
    return client

@app.get("/clients/", response_model=List[IndustrialClient])
def read_clients(session: Session = Depends(get_session)):
    clients = session.exec(select(IndustrialClient)).all()
    return clients

@app.get("/clients/{client_id}", response_model=IndustrialClient)
def read_client(client_id: int, session: Session = Depends(get_session)):
    client = session.get(IndustrialClient, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client