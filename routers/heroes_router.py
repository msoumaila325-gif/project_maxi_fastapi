from fastapi import  Path, Query, Body, HTTPException, APIRouter
from classes import HeroValidation, Hero
from heroes import HEROES
from utils import find_proper_hero_id
from starlette import status
from database import db_dependency
from sqlalchemy import text
from typing import Optional, List
from database import get_db, engine
from sqlalchemy.orm import Session
from fastapi import Depends
import models
from models import Heroes

router = APIRouter( # minuscule
    tags=["heroes"],
    prefix="/heroes"
)
# CREATE DATABASE

models.Base.metadata.create_all(bind=engine)


@router.get("/heartbeat")
def heartbeat(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "DATABASE CONNECTED"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/heroes", status_code=status.HTTP_200_OK)
async def get_all_heroes(db: Session = Depends(get_db)):
    return db.query(Heroes).order_by(Heroes.id.asc()).all()


# GET BY TYPE (AS QUERY PARAM)
@router.get("/type", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_type(db: Session = Depends(get_db), hero_type: Optional[str] = Query(None)):
    result = db.query(Heroes).filter(Heroes.type.ilike(f"%{hero_type}%")).all()
    return result


# return CAN bo empty

# GET BY RANK (AS QUERY PARAM)
@router.get("/rank", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_rank(db: Session = Depends(get_db), hero_rank: Optional[int] = Query(None, ge=0, le=100)):
    result = db.query(Heroes).filter(Heroes.rank >= hero_rank).all()
    return result


# return CAN bo empty

# GET ONE HERO BY ID (AS PATH PARAM)
@router.get("/id/{hero_id}", status_code=status.HTTP_200_OK)
async def get_one_hero_by_id(db: Session = Depends(get_db), hero_id: int = Path(ge=0, le=100)):
    hero_id = db.query(Heroes).filter(Heroes.id == hero_id).first()
    if hero_id is not None:
        return hero_id
    raise HTTPException(status_code=404, detail="Hero not found")


# GET ONE HERO BY NICkNANE
@router.get("/nick/{nick}", status_code=status.HTTP_200_OK)
async def get_one_hero_by_nick(db: Session = Depends(get_db), nick: str = Path()):
    result = db.query(Heroes).filter(Heroes.nick_name.ilike(f"%{nick}%")).all()
    return result


# return CAN bo empty


# Post/create (BY BODY)
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_hero(hero_body: HeroValidation = Body()):
    new_hero = Hero(**hero_body.model_dump())

    print(type(new_hero))
    HEROES.append(find_proper_hero_id(new_hero))


# UPDATE WITH PUT (BY BODY)
@router.put("/update/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_hero(db: Session = Depends(get_db), hero_id: int = Path(ge=1), hero_body: HeroValidation = Body()):
    hero_db = db.query(Heroes).filter(Heroes.id == hero_id).first()
    if hero_db is None:
        raise HTTPException(status_code=404, detail="Hero not found")

    hero_db.nick_name = hero_body.nick_name
    hero_db.full_name = hero_body.full_name
    hero_db.occupation = hero_body.occupation
    hero_db.powers = hero_body.powers
    hero_db.hobby = hero_body.hobby
    hero_db.type = hero_body.type
    hero_db.rank = hero_body.rank
    db.add(hero_db)
    db.commit()


# DELETE (BY ID AS PAHT PARAM)

@router.delete("/delete/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(db: Session = Depends(get_db), hero_id: int = Path(ge=0)):
    hero_db = db.query(Heroes).filter(Heroes.id == hero_id).first()
    if hero_db is not None:
        raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(hero_db)
    db.commit()

