from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey

from .base import Base
from .mixins import IdMixin
from .mixins import CreatedAtMixin


class Song(Base, IdMixin, CreatedAtMixin):
    __tablename__ = 'songs'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    duration_seconds: Mapped[int]
    title: Mapped[str]
