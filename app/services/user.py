from sqlalchemy.orm import Session

from app.repositories.user import UserRepo
from app.schemas.user import AddUserSchema
from app.models.user import User


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepo(db)

    def add_user(self, data: AddUserSchema) -> User:
        user_obj = User(**data.model_dump())
        return self.repo.create(user_obj)
