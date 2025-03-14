import os

from app.core.config import settings


class SongService:
    def __init__(self):
        self.dir_path = settings.SONGS_DIRECTORY_PATH
        SongService._create_dir_if_not_exists(self.dir_path)

    @staticmethod
    def _create_dir_if_not_exists(dir_path: str) -> None:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def save_song_file(self, file: bytes, rel_path: str) -> None:
        abs_path = self.dir_path + rel_path

        if os.path.exists(abs_path):
            raise FileExistsError

        with open(abs_path, 'wb') as f:
            f.write(file)
