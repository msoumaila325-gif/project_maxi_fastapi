from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends


# CREATE ENGINE
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://postgres:postgres@localhost:5434/dungeon_and_dragon"
)


# DEF ENGINE
engine = create_engine(SQLALCHEMY_DATABASE_URI)
#  DEF OF SESSION
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# CREATE BASE
Base = declarative_base()


# DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# DEPENDENCY ANNOTATED
db_dependency = Annotated[Session, Depends(get_db)]


def db_dependency():
    return SessionLocal()

