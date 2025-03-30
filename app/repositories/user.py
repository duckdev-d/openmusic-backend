from sqlalchemy import insert

from app.repositories.base import BaseRepo
from app.models.user import User
from app.models.assotiation_tables.user_song import UserSong


class UserRepo(BaseRepo[User]):
    def __init__(self, db):
        super().__init__(db, User)

    def get_by_username(self, username) -> User:
        user = self.db.query(User).where(User.username == username).first()
        return user

    def add_favourite(self, user_id: int, song_id: int) -> None:
        query = insert(UserSong).values(user_id=user_id, song_id=song_id)
        self.db.execute(query)
        # relation_obj = UserSong(user_id=user_id, song_id=song_id)
        # self.db.add(relation_obj)
        self.db.commit()
