from fastapi import APIRouter

from app.api.voting import voting_router


api_router = APIRouter(prefix="/api")

api_router.include_router(voting_router)