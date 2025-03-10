from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.db import get_session
from app.schemas.user import ShowUserSchema
from app.schemas.user import AddUserSchema
from app.services.user import UserService


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=ShowUserSchema)
def create_user(data: AddUserSchema, db: Session = Depends(get_session)):
    user_service = UserService(db)
    try:
        return user_service.add_user(data)
    except IntegrityError:
        return Response('Username in already occupied', status.HTTP_409_CONFLICT)


@router.get('/{username}', response_model=ShowUserSchema)
def get_user_by_username(username: str, db: Session = Depends(get_session)):
    user_service = UserService(db)
    user = user_service.get_user_by_username(username)
    if user is None:
        return Response(
            f'Could bot find user with username {username}', status.HTTP_404_NOT_FOUND
        )
    print(user)
    return user
