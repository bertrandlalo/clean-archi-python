from domain.ports.user import User, UserStatus
from domain.ports.user_repository import AbstractUserRepository
import uuid as uuid_lib

from domain.ports.uuid import AbstractUuid


class CreateNewUser:
    def __init__(
        self, user_repository: AbstractUserRepository, uuid=AbstractUuid
    ) -> None:
        self.user_repository = user_repository
        self.uuid = uuid

    def execute(self, name: str, status: UserStatus):
        user = User(
            name=name,
            status=status,
            uuid=self.uuid.make(),
        )
        self.user_repository.add(user)
