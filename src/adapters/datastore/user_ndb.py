from google.cloud import ndb
from domain.ports import User


class UserNDB(ndb.Model):
    name = ndb.StringProperty()
    status = ndb.StringProperty()

    @property
    def id(self):
        return self.key.to_legacy_urlsafe('h~').decode()

    def to_user(self):
        return User(name=self.name, status=self.status, uuid=self.id)
