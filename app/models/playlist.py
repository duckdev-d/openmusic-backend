from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import IdMixin
from .mixins import CreatedAtMixin


class Playlist(IdMixin, CreatedAtMixin, Base):
    __tablename__ = 'playlists'

    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    is_public: Mapped[bool] = mapped_column(default=False)

    songs: Mapped[list['Song']] = relationship(secondary='playlist_song')  # type: ignore # noqa: F821
