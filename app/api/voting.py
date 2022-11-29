import json
import uuid

from fastapi import APIRouter, Depends
from redis import Redis

from app.db.rd import get_database
from app.schemas.voting import Voting

voting_router = APIRouter(prefix="/voting")


@voting_router.post("/", status_code=201)
async def create_voting(voting: Voting, db: Redis = Depends(get_database)):  # создание голосования
    voting_id = str(uuid.uuid4())  # назначение id
    db.set(voting_id, json.dumps(voting.dict()))  # добавление данных в бд
    for option in voting.options:
        db.set(f"{voting_id}_option_{option.id}", 0)  # создание ключей голосов
    return {"voting_id": voting_id}


@voting_router.get("/{voting_id}")
async def get_voting_by_id(voting_id: str, db: Redis = Depends(get_database)):  # получение голосования
    voting_data = json.loads(db.get(voting_id))  # получение данных из бд
    result = []
    votes = 0
    for option in voting_data["options"]:  # проходим по вариантам ответов
        stat = int(db.get(f"{voting_id}_option_{option['id']}"))  # получаем кол-во голосов по варианту
        result.append({
            "name": option["name"],
            "stat": stat
        })  # собираем данные о варианте
        votes += stat  # собираем сумму голосов
    if votes == 0:  # если 0 голосов - то и проценты во всех вариантах 0
        for option in result:
            option["percent"] = 0.0
    else:
        for option in result:
            option["percent"] = option["stat"] * 100 / votes  # высчитываем процент
    return {"data": result}


@voting_router.post("/{voting_id}/{option_id}")
async def upvote(voting_id: str, option_id: int, db: Redis = Depends(get_database)):  # голосование за вариант
    db.incr(f"{voting_id}_option_{option_id}", 1)  # повышаем статистику варианта
    return None
