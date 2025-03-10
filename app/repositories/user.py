from app.repositories.base import BaseRepo
from app.models.user import User


class UserRepo(BaseRepo[User]):
    def __init__(self, db):
        super().__init__(db, User)

    def get_by_username(self, username) -> User:
        user = self.db.query(User).where(User.username == username).first()
        return user
