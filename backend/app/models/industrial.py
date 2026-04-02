from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class IndustrialClient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(index=True)
    sector: str  # e.g., Manufacturing, Logistics, Mining
    estimated_contract_value: float
    contact_email: str
    location: str = "East Rand, Gauteng"
    status: str = "Lead" # Lead, In-Progress, Closed
    created_at: datetime = Field(default_factory=datetime.utcnow)
