import os

import pytest

from app.core.config import settings
from tests.conftest import song_service
from tests.conftest import fake_song_file
from tests.conftest import fake_song_file_name


def test_add(song_service):
    fake_song_file = b'fake song file data'
    fake_song_file_name = '/testsong1.mp3'
    song_service._save_song_file(fake_song_file, fake_song_file_name)

    saved_song_path = settings.SONGS_DIRECTORY_PATH + fake_song_file_name
    with open(saved_song_path, 'rb') as f:
        assert f is not None


def test_add_existing(song_service, fake_song_file, fake_song_file_name):
    song_service._save_song_file(fake_song_file, fake_song_file_name)
    with pytest.raises(FileExistsError):
        song_service._save_song_file(fake_song_file, fake_song_file_name)


def test_delete(song_service, fake_song_file, fake_song_file_name):
    abs_path = settings.SONGS_DIRECTORY_PATH + fake_song_file_name
    with open(abs_path, 'wb') as f:
        f.write(fake_song_file)
    song_service._remove_song_file(fake_song_file_name)
    assert not os.path.exists(abs_path)


def test_delete_not_existing(song_service, fake_song_file_name):
    abs_path = settings.SONGS_DIRECTORY_PATH + fake_song_file_name
    with pytest.raises(FileNotFoundError):
        song_service._remove_song_file(fake_song_file_name)
