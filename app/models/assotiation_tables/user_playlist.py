from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from models.base import Base


UserPlaylist = Table(
    'user_playlist',
    Base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('playlist_id', ForeignKey('playlists.id')),
)
