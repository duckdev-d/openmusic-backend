from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import IdMixin
from .mixins import CreatedAtMixin


class User(IdMixin, CreatedAtMixin, Base):
    __tablename__ = 'users'

    username: Mapped[str]
    password_hash: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)

    favourite_songs: Mapped[list['Song']] = relationship(secondary='user_song')  # type: ignore # noqa: F821
    favourite_playlists: Mapped[list['Playlist']] = relationship(  # noqa: F821 # type: ignore
        secondary='user_playlist'
    )
