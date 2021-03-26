from google.cloud import ndb

from domain.ports.user import User


class UserNDB(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()

    @property
    def id(self):
        return self.key.to_legacy_urlsafe('h~').decode()

    def to_user(self):
        return User(first_name=self.first_name, last_name=self.last_name, uuid=self.id)
