import abc
from typing import List, Any, Optional

from domain.models.user import User
from domain.ports.uuid import AbstractUuid


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: Any) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self) -> List[User]:
        raise NotImplementedError


class InMemoryUserRepository(AbstractUserRepository):
    _users: List[User]

    def __init__(self) -> None:
        self._users = []

    def add(self, user: User):
        self._users.append(user)

    def get(self, uuid: Any) -> Optional[User]:
        for user in self._users:
            if user.uuid == uuid:
                return user

    def get_all(self) -> List[User]:
        return self._users

    # For test purposes only
    @property
    def users(self) -> List[User]:
        return self._users

    @users.setter
    def users(self, users: List[User]):
        self._users = users
