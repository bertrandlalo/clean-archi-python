from typing import List

from google.cloud import ndb

from domain.ports import User
from domain.ports.user.user_repository import AbstractUserRepository
from .user_ndb import UserNDB


class NDBUserRepository(AbstractUserRepository):

    def add(self, user: User):
        ndb_user = UserNDB(
            name=user.name, status=user.status
        )
        ndb_user.put()
        user.set_id(ndb_user.id)

    def get(self, uuid: str) -> User:
        user: UserNDB = ndb.Key(urlsafe=uuid).get()
        return user.to_user()

    def get_all(self) -> List[User]:
        ndb_user_list = UserNDB.query().fetch()
        return [ndb_user.to_user() for ndb_user in ndb_user_list]

    def new_untested_method(self):
        print('hey there')
        return True
