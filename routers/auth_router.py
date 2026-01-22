from fastapi import APIRouter, Body, Depends, HTTPException
from classes import PlayerValidation,Token
from models import Players
from database import get_db,db_dependency
from sqlalchemy.orm import Session
from fastapi import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

router = APIRouter()  # minuscule

# BEARER TOKEN DEPENDENCY FOR THE ENOPOINT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# BCRYPT CONFIG
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# jwt
# key GENERATE WITH COMMAND: openssl rand -hex 64
JWT_SECRET = "ca0f3471bcb942407c13bb5f6a7891524ef49d1ce1660b5924b6c832e45d07546e7276da0c426e184de5796db82ddf2d5e5164ecc1cd2d738ceb49ea6244bf66"
JWT_ALOD = "HS256"

#HELPER FAMCTION FOR LOGIN
def authenticate_Player(db: Session, username: str, password: str):
    found_Player = db.query(Players).filter(Players.username == username).first()
    if not found_Player:
        return False
    if not bcrypt_context.verify(password, found_Player.hashed_password):
        return False
    return found_Player

def create_token(username: str,user_id: int, expires_delta: timedelta):
    encoded_data = {"sub": username, "id": user_id}
    expiration = datetime.now(timezone.utc) + expires_delta
    encoded_data.update({ "exp": expiration.timestamp()})
    return jwt.encode(encoded_data, JWT_SECRET, algorithm=JWT_ALOD)

##
#FOR AUTH MIDDLEWARE
async  def get_current_Player(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALOD])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
##

@router.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def register_players(db: Session = Depends(get_db), player_body: PlayerValidation = Body()):
    new_player = Players(
        email=player_body.email,
        username=player_body.username,
        first_name=player_body.first_name,
        last_name=player_body.last_name,
        hashed_password=bcrypt_context.hash(player_body.password),
        is_active = True,
        role=player_body.role
    )
    db.add(new_player)
    db.commit()  
    return {
        "status": "success",
        "message": "Utilisateur enregistré avec succès"
    }
@router.post("/auth/login",response_model=Token, status_code=status.HTTP_200_OK)
async def login_player(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    Players_authenticated = authenticate_Player(db, form_data.username, form_data.password)
    if not Players_authenticated:
        return "Arong credentials"
    token = create_token(Players_authenticated.username, Players_authenticated.id, timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}
