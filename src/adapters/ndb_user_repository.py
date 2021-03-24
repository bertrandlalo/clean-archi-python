from google.cloud import ndb

from domain.ports.model import User
from domain.ports.user_repository import AbstractUserRepository


class UserNDB(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    uuid = ndb.StringProperty()


class NDBUserRepository(AbstractUserRepository):
    def add(self, user: User):
        with ndb.Client().context():
            ndb_user = UserNDB(
                first_name=user.first_name, last_name=user.last_name, uuid=user.uuid
            )
            ndb_user.put()

    def get(self, uuid: str) -> User:
        raise NotImplementedError