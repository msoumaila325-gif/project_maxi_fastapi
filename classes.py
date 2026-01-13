from typing import List, Optional,Literal
from pydantic import BaseModel, Field, constr, field_validator


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
AllowedRoles = Literal["controller", "defender", "leader", "striker"]

class PlayerValidation(BaseModel):
    email: str = Field(description = "Email address")
    username: str = Field(description = "Pseudo")
    first_name: str = Field(description = "First name")
    last_name: str = Field(description = "Family name")
    password: str = Field(description = "Password")
    role: AllowedRoles = Field(description = "Role of the player.Should be either controller,defander,leader or striker")
    # PRE VALIDATION
    @field_validator ("role", mode="before")
    def lower_case_role(cls, val: str) -> str:
        return val.lower()
   # CUSTOMIZATION OF DISPLAYED INFOS IN SWAGGER MODEL
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "maximis@gmail.com",
                "username": "mali",
                "first_name": "Maxi",
                "last_name": "Maiga",
                "password": "stromea",
                "role": "controller"
            }
        }
    }  