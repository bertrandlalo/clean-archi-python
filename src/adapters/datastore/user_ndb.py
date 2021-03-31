from google.cloud import ndb
from domain.models.user import User


class UserNDB(ndb.Model):
    uuid = ndb.StringProperty()
    name = ndb.StringProperty()
    status = ndb.StringProperty()

    @property
    def id(self):
        return self.key.to_legacy_urlsafe("h~").decode()

    def to_user(self):
        return User(name=self.name, status=self.status, uuid=self.uuid)

    @classmethod
    def from_user(cls, user: User) -> "UserNDB":
        return cls(uuid=user.uuid, name=user.name, status=user.status)