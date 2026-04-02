from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class IndustrialClient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(index=True)
    sector: str  # Manufacturing, Logistics, etc.
    contract_value: float
    contact_person: str
    email: str
    location: str = "East Rand, Gauteng"
    status: str = "Lead"
    last_outreach: datetime = Field(default_factory=datetime.utcnow)