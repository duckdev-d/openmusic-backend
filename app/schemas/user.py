from pydantic import BaseModel
from pydantic import constr


class AddUserSchema(BaseModel):
    username: constr(min_length=3, max_length=30)  # type: ignore
    password_hash: str
    is_admin: bool = False


class ShowUserSchema(BaseModel):
    username: constr(min_length=3, max_length=30)  # type: ignore
    is_admin: bool = False
