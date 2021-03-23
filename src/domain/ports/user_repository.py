import abc
from typing import List
from .model import User


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: str) -> User:
        raise NotImplementedError

    @abc.abstractproperty
    def users(self) -> List[User]:
        raise NotImplementedError


class InMemoryUserRepository(AbstractUserRepository):
    _users: List[User]

    def __init__(self) -> None:
        self._users = []

    def add(self, user: User):
        self._users.append(user)

    def get(self, uuid: str) -> User:
        raise NotImplementedError

    @property
    def users(self) -> List[User]:
        return self._users
