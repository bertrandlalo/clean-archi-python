from google.cloud import ndb

from adapters.datastore.ndb_user_repository import NDBUserRepository
from domain.ports.model import User

user = User(first_name="patrice", last_name="bertrand")


def test_can_add_user():
    client = ndb.Client()
    with client.context():
        ndb_user_repository = NDBUserRepository(project_id='next-experquiz-com')
        number_users_before_add = len(ndb_user_repository.users)
        ndb_user_repository.add(user)
        assert len(ndb_user_repository.users) == number_users_before_add + 1


def test_can_get_user():
    client = ndb.Client()
    with client.context():
        ndb_user_repository = NDBUserRepository(project_id='next-experquiz-com')
        user_from_ndb = ndb_user_repository.get(user.id)
        assert user_from_ndb == user


def test_can_get_all_users():
    client = ndb.Client()
    with client.context():
        all_users = NDBUserRepository(project_id='next-experquiz-com').users
        assert type(all_users) == list
        assert len(all_users) > 0
        for user in all_users:
            assert type(user) == User
