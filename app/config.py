from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    redis_url: str = Field(..., env="REDIS_URL")
    redis_port: int = Field(..., env="REDIS_PORT")

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
