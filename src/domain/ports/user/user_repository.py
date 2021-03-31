import abc
from typing import List, Any

from .model import User
from ..uuid import AbstractUuid


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: Any) -> User:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def users(self) -> List[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self) -> List[User]:
        raise NotImplementedError


class InMemoryUserRepository(AbstractUserRepository):
    _users: List[User]

    def __init__(self, uuid_generator: AbstractUuid) -> None:
        self.uuid_generator = uuid_generator
        self._users = []

    def add(self, user: User):
        user.set_id(self.uuid_generator.make())
        self._users.append(user)

    def get_all(self) -> List[User]:
        return self._users

    # For test purposes only
    @property
    def users(self) -> List[User]:
        return self._users

    @users.setter
    def users(self, users: List[User]):
        self._users = users
