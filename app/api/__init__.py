from fastapi import APIRouter

from app.api.users import router as user_router
from app.api.token import router as token_router


api = APIRouter(prefix='/api')

api.include_router(user_router)
api.include_router(token_router)
