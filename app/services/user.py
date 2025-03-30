from sqlalchemy.orm import Session

from app.repositories.user import UserRepo
from app.schemas.user import AddUserSchema
from app.schemas.song import ShowSongSchema
from app.models.user import User
from app.core.security import get_password_hash


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepo(db)

    def add_user(self, data: AddUserSchema) -> User:
        password_hash = get_password_hash(data.password)
        user_obj = User(username=data.username, password_hash=password_hash)
        return self.repo.create(user_obj)

    def get_user_by_username(self, username: str) -> User:
        return self.repo.get_by_username(username)

    def get_all_users(self) -> list[User]:
        return self.repo.get_all()

    def add_song_to_favourites(self, song_id: int, user_id: int) -> None:
        self.repo.add_favourite_song(user_id=user_id, song_id=song_id)
        print(self.repo.db.query(User).where(User.id == user_id).first())

    def get_favourite_songs(self, user_id) -> list[ShowSongSchema]:
        return self.repo.get_favourite_songs(user_id=user_id)
