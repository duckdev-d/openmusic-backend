from sqlalchemy.orm import joinedload

from app.repositories.base import BaseRepo
from app.models.song import Song


class SongRepo(BaseRepo[Song]):
    def __init__(self, db):
        super().__init__(db, Song)

    def get_all(self):
        query = self.db.query(Song).options(joinedload(Song.artist))
        return query.all()
