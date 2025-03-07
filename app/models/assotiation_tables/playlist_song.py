from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from ..base import Base


PlaylistSong = Table(
    'playlist_song',
    Base.metadata,
    Column('playlist_id', ForeignKey('playlists.id')),
    Column('song_id', ForeignKey('songs.id')),
)
