from typing import Generator
from typing import Any
import shutil

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.repositories.user import UserRepo
from app.models.user import User
from app.services.song import SongService


@pytest.fixture(scope='function')
def test_db():
    #  unsused imports needed for initializing models
    #  and adding them to Base.metadata
    from app.models.playlist import Playlist  # noqa: F401
    from app.models.user import User  # noqa: F401
    from app.models.song import Song  # noqa: F401
    from app.models.assotiation_tables.playlist_song import PlaylistSong  # noqa: F401
    from app.models.assotiation_tables.user_playlist import UserPlaylist  # noqa: F401
    from app.models.assotiation_tables.user_song import UserSong  # noqa: F401
    from app.models.base import Base

    db_url = settings.DB_URL
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    yield db

    db.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='function')
def song_service(test_db) -> Generator[SongService, Any, Any]:
    yield SongService(test_db)
    shutil.rmtree(settings.SONGS_DIRECTORY_PATH)


@pytest.fixture(scope='function')
def user_repo(test_db):
    return UserRepo(test_db)


@pytest.fixture(scope='function')
def test_user():
    return User(username='bob', password_hash='s564dfg8d4s6g4', is_admin=False)


@pytest.fixture(scope='function')
def fake_song_file():
    return b'fake song file data'


@pytest.fixture(scope='function')
def fake_song_file_name():
    return '/testsong1.mp3'
