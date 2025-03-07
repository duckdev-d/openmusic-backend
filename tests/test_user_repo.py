from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.repositories.user import UserRepo
from app.core.test_config import test_settings

#  unsused imports needed for initializing models
#  and adding them to Base.metadata
from app.models.playlist import Playlist
from app.models.user import User
from app.models.song import Song
from app.models.assotiation_tables.playlist_song import PlaylistSong
from app.models.assotiation_tables.user_playlist import UserPlaylist
from app.models.assotiation_tables.user_song import UserSong
from app.models.base import Base


@fixture(scope='function')
def test_db():
    db_url = test_settings.DB_URL
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(engine)


@fixture(scope='function')
def user_repo(test_db):
    return UserRepo(test_db)


def test_get_all_empty(user_repo):
    result = user_repo.get_all()

    assert result == []


def test_get_all_with_data(test_db, user_repo):
    test_db.add_all(
        [
            User(username='bob', password_hash='adgfdgagad84665adfgdf', is_admin=True),
            User(
                username='cris', password_hash='adgfdgagad84665adfgdf', is_admin=False
            ),
        ]
    )
    test_db.commit()
    result = user_repo.get_all()

    assert len(result) == 2
    assert result[0].is_admin
    assert result[1].username == 'cris'
