from typing import get_args, List

from domain.models.user import UserStatus, User
from domain.ports.user_repository import AbstractUserRepository
from google.cloud import ndb


class UserNDB(ndb.Model):
    name = ndb.StringProperty()
    status = ndb.StringProperty(choices=get_args(UserStatus))
    uuid = ndb.StringProperty()

    def to_user(self) -> User:
        return User(
            name=self.name,
            status=self.status,
            uuid=self.uuid,
        )


class NDBUserRepository(AbstractUserRepository):

    def add(self, user: User):
        ndb_user = UserNDB(name=user.name, status=user.status, uuid=user.uuid, id=user.uuid)
        ndb_user.put()

    def get(self, uuid: str) -> User:
        ndb_user: UserNDB = UserNDB.get_by_id(uuid)
        return ndb_user.to_user()

    def get_all(self) -> List[User]:
        users_ndb: List[UserNDB] = UserNDB.query().fetch()
        return [user_ndb.to_user() for user_ndb in users_ndb]


def flush_all_users():
    ndb.delete_multi(UserNDB.query().fetch(keys_only=True))
