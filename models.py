from database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY


class Heroes(Base):
    __tablename__ = "heroes"
    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    nick_name = Column(String)
    full_name = Column(String, nullable=False)
    occupation = Column(ARRAY(String))
    powers = Column(ARRAY(String))
    hobby = Column(ARRAY(String))
    type = Column(String)
    rank = Column(Integer)

    
class player(Base):
    __tablename__ = "player"
    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
