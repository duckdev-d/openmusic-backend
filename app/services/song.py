import os
from uuid import uuid4
from io import BytesIO

from sqlalchemy.orm import Session
from mutagen.mp3 import MP3
from fastapi import UploadFile

from app.core.config import settings
from app.repositories.song import SongRepo
from app.schemas.song import AddSongSchema
from app.models.song import Song


class SongService:
    def __init__(self, db: Session):
        self.repo = SongRepo(db)
        self.dir_path = settings.SONGS_DIRECTORY_PATH
        SongService._create_dir_if_not_exists(self.dir_path)

    @staticmethod
    def _create_dir_if_not_exists(dir_path: str) -> None:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def _get_song_duration_seconds(file: bytes) -> int:
        file = BytesIO(file)
        song_duration_milliseconds = MP3(file).info.length
        song_duration_seconds = song_duration_milliseconds // 1000
        return song_duration_seconds

    def _save_song_file(self, file: bytes, rel_path: str) -> None:
        abs_path = self.dir_path + rel_path
        if os.path.exists(abs_path):
            raise FileExistsError
        with open(abs_path, 'wb') as f:
            f.write(file)

    def _remove_song_file(self, rel_path: str) -> None:
        abs_path = self.dir_path + rel_path
        if not os.path.exists(abs_path):
            raise FileNotFoundError
        os.remove(abs_path)

    def add_song(
        self, file: UploadFile, user_id: int, song_data: AddSongSchema
    ) -> None:
        file_bytes = file.file.read()
        file_id = str(uuid4())
        rel_path = f'/{file_id}.mp3'
        self._save_song_file(file_bytes, rel_path)
        song_title = song_data.title
        song_duration_seconds = self._get_song_duration_seconds(file_bytes)
        song_obj = Song(
            user_id=user_id,
            duration_seconds=song_duration_seconds,
            title=song_title,
            relative_file_path=rel_path,
        )
        self.repo.create(song_obj)
