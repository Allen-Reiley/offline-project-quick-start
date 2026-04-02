from sqlmodel import create_engine, Session, SQLModel
from .config import settings

# Uses the DATABASE_URL from your .env
engine = create_engine(settings.DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
