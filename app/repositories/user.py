from app.repositories.base import BaseRepo
from app.models.user import User


class UserRepo(BaseRepo):
    def __init__(self, db):
        super().__init__(db, User)
