from pydantic import BaseModel
from pydantic import constr


class AddSongSchema(BaseModel):
    title: str = constr(min_length=5)
