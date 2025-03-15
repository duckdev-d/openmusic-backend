from pydantic import BaseModel
from pydantic import constr

from app.schemas.user import ShowUserSchema


class AddSongSchema(BaseModel):
    title: str = constr(min_length=5)


class ShowSongSchema(AddSongSchema):
    artist: ShowUserSchema
