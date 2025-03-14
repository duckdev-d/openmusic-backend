import shutil
from typing import Generator
from typing import Any

import pytest

from app.services.song import SongService
from app.core.config import settings


@pytest.fixture(scope='function')
def song_service() -> Generator[SongService, Any, Any]:
    yield SongService()
    shutil.rmtree(settings.SONGS_DIRECTORY_PATH)


def test_add(song_service):
    fake_song_file = b'fake song file data'
    fake_song_file_name = '/testsong1.mp3'
    song_service.save_song_file(fake_song_file, fake_song_file_name)

    saved_song_path = settings.SONGS_DIRECTORY_PATH + fake_song_file_name
    with open(saved_song_path, 'rb') as f:
        assert f is not None


def test_add_existing(song_service):
    fake_song_file = b'fake song file data'
    fake_song_file_name = '/testsong1.mp3'

    song_service.save_song_file(fake_song_file, fake_song_file_name)
    with pytest.raises(FileExistsError):
        song_service.save_song_file(fake_song_file, fake_song_file_name)
