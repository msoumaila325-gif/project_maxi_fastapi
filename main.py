from fastapi import FastAPI, Path, Query

from heroes import HEROES

app = FastAPI()  # minuscule

@app.get("/")    # minuscule
async def heartbeat():
    return "App running"
# get_all

@app.get("/heroes")
async def get_all_heroes():
    return HEROES

 # GET BY TYPE (AS QUERY PARAM)
@app.get("/heroes/type")
async def get_all_heroes(hero_type: str = Query()):
    result = []
    for hero in HEROES:
        if hero_type.casefold() in hero["type"].casefold():
            result.append(hero)
    return result

# GET BY RANK (AS QUERY PARAM)
@app.get("/heroes/rank")
async def get_all_heroes(hero_rank: int = Query()):
    result = []
    for hero in HEROES:
        if hero.get("rank") >= hero_rank:
            result.append(hero)
    return result

# GET ONE HERO BY ID (AS PATH PARAM)
@app.get("/heroes/id/{hero-id}")
async def get_one_hero_by_id(hero_id: int = Path()):
    result = []
    for hero in HEROES:
        if hero.get("id") == hero_id:
            result.append(hero)
    return hero