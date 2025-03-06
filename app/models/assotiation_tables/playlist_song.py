from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from models.base import Base


PlaylistSong = Table(
    'user_playlist',
    Base.metadata,
    Column('playlist_id', ForeignKey('playlists.id')),
    Column('song_id', ForeignKey('songs.id')),
)
