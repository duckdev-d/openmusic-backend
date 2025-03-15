import os

from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.song import SongRepo


class SongService:
    def __init__(self, db: Session):
        self.repo = SongRepo(db)
        self.dir_path = settings.SONGS_DIRECTORY_PATH
        SongService._create_dir_if_not_exists(self.dir_path)

    @staticmethod
    def _create_dir_if_not_exists(dir_path: str) -> None:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

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
