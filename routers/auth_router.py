from fastapi import APIRouter, Body, Depends
from classes import PlayerValidation
from models import Players
from database import get_db,db_dependency
from sqlalchemy.orm import Session

router = APIRouter()  # minuscule
@router.post("/auth/register")
async def register_players(db: Session = Depends(get_db), player_body: PlayerValidation = Body()):
    new_player = Players(
        email=player_body.email,
        username=player_body.username,
        first_name=player_body.first_name,
        last_name=player_body.last_name,
        hashed_password=player_body.password,
        is_active = True,
        role=player_body.role
    )
    db.add(new_player)
    db.commit()

