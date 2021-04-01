from adapters.ndb_user_repository import NDBUserRepository, flush_all_users
from domain.models.user import User
from google.cloud import ndb

client = ndb.Client()

with client.context():
    flush_all_users()

user = User(name="patrice", status="active", uuid="uuid_pat")


def test_can_add_user():
    with client.context():
        ndb_user_repository = NDBUserRepository()
        ndb_user_repository.add(user)
        assert len(ndb_user_repository.get_all()) == 1


def test_can_get_user():
    with client.context():
        ndb_user_repository = NDBUserRepository()
        user_from_ndb = ndb_user_repository.get(user.uuid)
        assert user_from_ndb == user


def test_can_get_all_users():
    with client.context():
        all_users = NDBUserRepository().get_all()
        assert type(all_users) == list
        assert len(all_users) > 0
        for user in all_users:
            assert type(user) == User
