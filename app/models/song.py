from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey

from app.models.base import Base
from app.models.mixins import IdMixin
from app.models.mixins import CreatedAtMixin


class Song(Base, IdMixin, CreatedAtMixin):
    __tablename__ = 'songs'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    duration_seconds: Mapped[int]
    title: Mapped[str]
    relative_file_path: Mapped[str]
