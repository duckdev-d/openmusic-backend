import pytest

from app.repositories.user import UserRepo
from app.models.user import User
from tests.conftest import test_db
from tests.conftest import user_repo
from tests.conftest import test_user


def test_get_all_empty(user_repo):
    result = user_repo.get_all()

    assert result == []


def test_get_all_with_data(test_db, user_repo):
    test_db.add_all(
        [
            User(
                username='bob', password_hash='adgfdgagad84665adfgdfjfg', is_admin=True
            ),
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


def test_get_by_id(user_repo, test_db, test_user):
    test_db.add(test_user)
    test_db.commit()
    result = user_repo.get_by_id(1)
    print(result)

    assert result is not None
    assert result.id == 1
    assert result.username == 'bob'


def test_get_by_id_not_existing(user_repo):
    result = user_repo.get_by_id(15)

    assert result is None


def test_create(user_repo, test_db, test_user):
    result = user_repo.create(test_user)
    user = test_db.query(User).first()

    assert result.id == 1
    assert user is not None
    assert user.id == 1


def test_delete(user_repo, test_db, test_user):
    test_db.add(test_user)
    test_db.commit()

    result = user_repo.delete(test_user)
    user = test_db.query(User).first()

    assert user is None
    assert result is None


def test_delete_not_existing(user_repo, test_user):
    with pytest.raises(Exception):
        user_repo.delete(test_user)
