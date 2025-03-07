from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    url=settings.DB_URL,
    echo=True,
)


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def set_db():
    from app.models.user import User
    from app.models.song import Song
    from app.models.playlist import Playlist
    from app.models.assotiation_tables.playlist_song import PlaylistSong
    from app.models.assotiation_tables.user_playlist import UserPlaylist
    from app.models.assotiation_tables.user_song import UserSong
    from app.models.base import Base

    Base.metadata.create_all(engine)


def drop_db():
    from app.models.base import Base

    Base.metadata.drop_all(engine)
