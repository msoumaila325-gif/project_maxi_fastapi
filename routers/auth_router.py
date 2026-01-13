from fastapi import APIRouter, Body
from classes import PlayerValidation


router = APIRouter()  # minuscule
@router.post("/auth/register")
async def register_player(player_body: PlayerValidation = Body()):
    return player_body