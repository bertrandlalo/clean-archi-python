from typing import List

from google.cloud import ndb

from domain.ports.model import User
from domain.ports.user_repository import AbstractUserRepository
from .user_ndb import UserNDB


class NDBUserRepository(AbstractUserRepository):
    def __init__(self, project_id: str):
        self.project_id = project_id

    def add(self, user: User):
        ndb_user = UserNDB(
            first_name=user.first_name, last_name=user.last_name
        )
        ndb_user.put()
        user.set_id(ndb_user.id)

    def get(self, uuid: str) -> User:
        user: UserNDB = ndb.Key(urlsafe=uuid).get()
        return user.to_user()

    @property
    def users(self) -> List[User]:
        ndb_user_list = UserNDB.query().fetch()
        return [ndb_user.to_user() for ndb_user in ndb_user_list]
