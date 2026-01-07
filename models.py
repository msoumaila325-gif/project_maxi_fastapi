from database import Base
from sqlalchemy import Column, Integer, String
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

    