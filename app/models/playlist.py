from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database import Base
from models.mixins import IdMixin
from models.mixins import CreatedAtMixin


class Playlist(IdMixin, CreatedAtMixin, Base):
    __tablename__ = 'playlists'

    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    is_public: Mapped[bool] = mapped_column(default=False)
