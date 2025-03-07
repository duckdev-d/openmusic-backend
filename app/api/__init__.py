from fastapi import APIRouter

from app.api.users import router as user_router


api = APIRouter(prefix='/api')

api.include_router(user_router)
