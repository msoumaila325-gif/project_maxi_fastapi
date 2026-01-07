from typing import List
from classes import Hero
import csv


HEROES: List[Hero] = [
    Hero(
        id=1,
        nick_name="Scanbo",
        full_name="Scanlan Shorthalt",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=48
    ),

    Hero(
        id=2,
        nick_name="neymar",
        full_name="barcelos neymar",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=71
    ),

    Hero(
        id=3,
        nick_name="soumaila",
        full_name="maiga",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="mali",
        rank=25
    ),
    Hero(
        id=4,
        nick_name="mamady",
        full_name="camara",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=39
    ),
    Hero(
        id=5,
        nick_name="Scanbo",
        full_name="Scanlan Shorthalt",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency",  "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=48
    ),
    Hero(
        id=6,
        nick_name="Scanbo",
        full_name="Scanlan Shorthalt",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=48
    ),
    Hero(
        id=7,
        nick_name="Scanbo",
        full_name="Scanlan Shorthalt",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=48
    ),
    Hero(
        id=8,
        nick_name="Scanbo",
        full_name="Scanlan Shorthalt",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=48
    ),
    Hero(
        id=9,
        nick_name="Scanbo",
        full_name="Scanlan Shorthalt",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Arcane magic proficiency", "Lute playing", "Charisma"],
        hobby=["Singing", "Having sex"],
        type="Casanova",
        rank=48
    )
]
# CREATE A CSV FILE WITH ALL HEROES
def format_array(py_list):
    return '{' + ', '.join(f'"{item}"' for item in py_list) + '}'

with open('heroes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # HEROES
    writer.writerow(['id', 'nick_name', 'full_name', 'occupation', 'powers', 'hobby', 'type', 'rank'])
    # DATA
    for hero in HEROES:
        writer.writerow([hero.id, hero.nick_name, hero.full_name, format_array(hero.occupation), format_array(hero.powers),
                         format_array(hero.hobby), hero.type, hero.rank])