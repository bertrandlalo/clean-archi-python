import abc
from typing import List
from domain.ports.user import User


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError


class InMemoryUserRepository(AbstractUserRepository):
    _users: List[User]

    def __init__(self):
        self._users = []

    def add(self, user: User):
        self._users.append(user)

    # For test purposes only
    @property
    def users(self) -> List[User]:
        return self._users
