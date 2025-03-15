from app.repositories.base import BaseRepo
from app.models.song import Song


class SongRepo(BaseRepo[Song]):
    def __init__(self, db):
        super().__init__(db, Song)
