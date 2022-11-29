from redis import Redis

from app.config import get_settings


class DB:
    rd_client = Redis(host=get_settings().redis_url, port=get_settings().redis_port, db=0)


db = DB()


def get_database():
    return db.rd_client
