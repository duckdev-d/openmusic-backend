from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.db import get_session
from app.models.user import User
from app.schemas.user import ShowUserSchema
from app.schemas.user import AddUserSchema
from app.services.user import UserService
from app.core.security import get_current_user


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=ShowUserSchema)
def create_user(data: AddUserSchema, db: Session = Depends(get_session)):
    user_service = UserService(db)
    try:
        return user_service.add_user(data)
    except IntegrityError:
        return Response('Username in already occupied', status.HTTP_409_CONFLICT)


@router.get('/', response_model=list[ShowUserSchema])
def get_all_users(
    current_user: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_session),
):
    user_service = UserService(db)
    users = user_service.get_all_users()
    return users


@router.post('/favourite-songs')
def add_favourite(
    song_id: int,
    current_user: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_session),
):
    user_service = UserService(db)
    user_service.add_song_to_favourites(song_id=song_id, user_id=current_user.id)
    return Response('Done', status.HTTP_201_CREATED)


@router.get('/favourite-songs')
def get_favourite_songs(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_session),
):
    user_service = UserService(db)
    return user_service.get_favourite_songs(current_user.id)


@router.get('/{username}', response_model=ShowUserSchema)
def get_user_by_username(
    username: str,
    current_user: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_session),
):
    user_service = UserService(db)
    user = user_service.get_user_by_username(username)
    if user is None:
        return Response(
            f'Could bot find user with username {username}', status.HTTP_404_NOT_FOUND
        )
    print(user)
    return user
