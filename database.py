from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends

# URL de connexion
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://postgres:postgres@localhost:5434/dungeon_and_dragon"
)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# La fonction qui génère la session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# L'annotation à utiliser dans tes routes FastAPI
# Exemple : @app.get("/") def read(db: db_dependency):
db_dependency = Annotated[Session, Depends(get_db)]