from fastapi import APIRouter, Body, Depends
from classes import PlayerValidation
from models import Players
from database import get_db,db_dependency
from sqlalchemy.orm import Session
from fastapi import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()  # minuscule

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#HELPER FAMCTION FOR LOGIN
def authenticate_Player(db: Session, username: str, password: str):
    found_Player = db.query(Players).filter(Players.username == username).first(  )
    if not found_Player:
        return False
    if not bcrypt_context.verify(password, found_Player.hashed_password):
        return False
    return found_Player
@router.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def register_players(db: Session = Depends(get_db), player_body: PlayerValidation = Body()):
    new_player = Players(
        email=player_body.email,
        username=player_body.username,
        first_name=player_body.first_name,
        last_name=player_body.last_name,
        hashed_password=bcrypt_context.hash(player_body.password,),
        is_active = True,
        role=player_body.role
    )
    db.add(new_player)
    db.commit()
    return {
        "status": "success",
        "message": "Utilisateur enregistré avec succès"
    }
@router.post("/auth/login")
async def login_players(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    Players_authenticated = authenticate_Player(db,form_data.username, form_data.password)
    if not Players_authenticated:
        return "wrong username or password"
    return "success"
