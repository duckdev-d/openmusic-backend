from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey

from app.core.db import Base
from models.mixins import IdMixin
from models.mixins import CreatedAtMixin


class Song(IdMixin, CreatedAtMixin, Base):
    __tablename__ = 'songs'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    duratinon_seconds: Mapped[int]
    title: Mapped[str]
