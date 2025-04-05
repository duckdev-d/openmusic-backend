from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from app.models.base import Base


UserSong = Table(
    'user_song',
    Base.metadata,
    Column('user_id', ForeignKey('users.id', ondelete='CASCADE')),
    Column('song_id', ForeignKey('songs.id', ondelete='CASCADE')),
)
