from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from app.core.db import Base


UserSong = Table(
    'user_song',
    Base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('song_id', ForeignKey('songs.id')),
)
