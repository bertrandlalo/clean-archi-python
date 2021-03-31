from google.cloud import ndb

from adapters.datastore.ndb_user_repository import NDBUserRepository
from domain.ports import User

user = User(name="patrice bertrand", status="active")


def test_can_add_user():
    client = ndb.Client()
    with client.context():
        ndb_user_repository = NDBUserRepository()
        number_users_before_add = len(ndb_user_repository.get_all())
        ndb_user_repository.add(user)
        assert len(ndb_user_repository.get_all()) == number_users_before_add + 1


def test_can_get_user():
    client = ndb.Client()
    with client.context():
        ndb_user_repository = NDBUserRepository()
        user_from_ndb = ndb_user_repository.get(user.id)
        assert user_from_ndb == user


def test_can_get_all_users():
    client = ndb.Client()
    with client.context():
        all_users = NDBUserRepository().get_all()
        assert type(all_users) == list
        assert len(all_users) > 0
        for user in all_users:
            assert type(user) == User
