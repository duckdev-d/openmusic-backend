from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import Form
from fastapi import status
from sqlalchemy.orm import Session

from app.core.db import get_session
from app.core.security import get_current_user
from app.services.song import SongService
from app.schemas.song import AddSongSchema
from app.schemas.song import ShowSongSchema


router = APIRouter(prefix='/songs', tags=['songs'])


@router.post('/', status_code=status.HTTP_201_CREATED)
def upload_song(
    file: UploadFile,
    title: Annotated[str, Form(...)],
    db: Annotated[Session, Depends(get_session)],
    current_user: Annotated[str, Depends(get_current_user)],
):
    song_service = SongService(db)
    song_data = AddSongSchema(title=title)
    song_service.add_song(file=file, user_id=current_user.id, song_data=song_data)
    return 'created'


@router.get('/', response_model=list[ShowSongSchema])
def get_all_songs(
    db: Annotated[Session, Depends(get_session)],
    current_user: Annotated[str, Depends(get_current_user)],
):
    song_service = SongService(db)
    return song_service.get_all_songs()


@router.get('/{song_id}')
def get_song(
    song_id,
    db: Annotated[Session, Depends(get_session)],
    current_user: Annotated[str, Depends(get_current_user)],
):
    song_service = SongService(db)
    return song_service.get_song_file_by_id(song_id)
