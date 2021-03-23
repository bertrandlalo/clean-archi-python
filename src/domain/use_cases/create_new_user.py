from src.domain.ports.uuid import AbstractUuid
from src.domain.ports.user_repository import AbstractUserRepository
from src.domain.ports.model import User


class CreateNewUser:
    def __init__(
        self, user_repository: AbstractUserRepository, uuid=AbstractUuid
    ) -> None:
        self.user_repository = user_repository
        self.uuid = uuid

    def execute(self, first_name: str, last_name: str):
        uuid = self.uuid.make()
        user = User(first_name, last_name, uuid)
        self.user_repository.add(user)
