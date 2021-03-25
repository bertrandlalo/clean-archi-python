from domain.ports.uuid import AbstractUuid
from domain.ports.user_repository import AbstractUserRepository
from domain.ports.model import User


class CreateNewUser:
    def __init__(
        self, user_repository: AbstractUserRepository, uuid=AbstractUuid
    ) -> None:
        self.user_repository = user_repository


    def execute(self, first_name: str, last_name: str):
        user = User(first_name, last_name)
        self.user_repository.add(user)
