from pydantic import BaseModel
from pydantic import constr
from pydantic import ConfigDict


class ShowUserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: constr(min_length=3, max_length=30)  # type: ignore
    is_admin: bool = False


class AddUserSchema(ShowUserSchema):
    password: str
