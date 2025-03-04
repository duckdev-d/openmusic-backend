from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.db import Base
from models.mixins import IdMixin
from models.mixins import CreatedAtMixin
from models.song import Song
from models.playlist import Playlist
from models.assotiation_tables import user_song
from models.assotiation_tables import user_playlist


class User(IdMixin, CreatedAtMixin, Base):
    __tablename__ = 'users'

    username: Mapped[str]
    password_hash: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)

    favourite_songs = Mapped[list[Song]] = relationship(secondary=user_song)
    favourite_playlists = Mapped[list[Playlist]] = relationship(secondary=user_playlist)
