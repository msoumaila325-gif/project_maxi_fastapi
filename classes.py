from typing import List, Optional
from pydantic import BaseModel, Field, constr


class Hero:
    id: int
    nick_name: str
    full_name: str
    occupation: list[str]
    powers: list[str]
    hobby: list[str]
    type: str
    rank: int
    def __init__(self, id, nick_name, full_name, occupation, powers, hobby, type, rank):
        self.id = id
        self.nick_name = nick_name
        self.full_name = full_name
        self.occupation = occupation
        self.powers = powers
        self.hobby = hobby
        self.type = type
        self.rank = rank

class HeroValidation(BaseModel):
    id: Optional[int] = Field(default=None, ge=0,description="ID is not needed en creation")
    nick_name: str = Field(min_length=3)
    full_name: str = Field(min_length=3)
    occupation: List[constr(min_length=3)]
    powers: List[constr(min_length=3)]
    hobby: List[constr(min_length=3)]
    type: str = Field(min_length=3)
    rank: int = Field(ge=0, le=100)
    model_config = {
        "json_schema_extra": {
            "example": {
                "nick_name": ["Scanbo"],
                "full_name": ["Scanlan Shorthalt"],
                "occupation": ["Wizard", "Adventurer", "Deity"],
                "powers": ["Arcane magic proficiency", "Lute playing", "Charisma"],
                "hobby": ["Singing", "Having sex"],
                "type": "Casanova",
                "rank": 48
        }
        }

        }
