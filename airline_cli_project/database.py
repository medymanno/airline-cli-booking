from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///airline.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    # Import models inside function to avoid circular import
    from airline_cli_project import models  
    Base.metadata.create_all(engine)

def get_session():
    """Return a new SQLAlchemy session."""
    return SessionLocal()
