import abc
from typing import List, Any, Optional

from domain.models.user import User


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: str) -> Optional[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_name(self, name: str) -> Optional[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self) -> List[User]:
        raise NotImplementedError


class InMemoryUserRepository(AbstractUserRepository):
    _users: List[User]

    def __init__(self, users: Optional[List[User]] = None) -> None:
        self._users = users or []

    def add(self, user: User):
        self._users.append(user)

    def get_all(self) -> List[User]:
        return self._users

    def get(self, uuid: str) -> Optional[User]:
        for user in self._users:
            if user.uuid == uuid:
                return user

    def get_by_name(self, name: str) -> Optional[User]:
        return next((user for user in self.users if user.name == name), None)

    # For test purposes only
    @property
    def users(self) -> List[User]:
        return self._users

    @users.setter
    def users(self, users: List[User]):
        self._users = users
