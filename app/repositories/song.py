from sqlalchemy.orm import joinedload
from sqlalchemy import select

from app.repositories.base import BaseRepo
from app.models.song import Song


class SongRepo(BaseRepo[Song]):
    def __init__(self, db):
        super().__init__(db, Song)

    def get_all(self):
        query = self.db.query(Song).options(joinedload(Song.artist))
        return query.all()

    def search(self, string: str):
        query = select(Song).where(Song.title.ilike(f'%{string}%'))
        return self.db.execute(query).scalars().all()
