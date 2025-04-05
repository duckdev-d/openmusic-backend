from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from app.models.base import Base


PlaylistSong = Table(
    'playlist_song',
    Base.metadata,
    Column('playlist_id', ForeignKey('playlists.id', ondelete='CASCADE')),
    Column('song_id', ForeignKey('songs.id', ondelete='CASCADE')),
)
