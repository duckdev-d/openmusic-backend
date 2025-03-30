from typing import TYPE_CHECKING

from pydantic import BaseModel
from pydantic import constr
from pydantic import ConfigDict


if TYPE_CHECKING:
    from app.schemas.user import ShowUserSchema


class AddSongSchema(BaseModel):
    title: str = constr(min_length=5)


class ShowSongSchema(AddSongSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    duration_seconds: int
    artist: 'ShowUserSchema'
    title: str
