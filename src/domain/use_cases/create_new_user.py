from domain.ports.user import User, UserStatus
from domain.ports.user.user_repository import AbstractUserRepository


class CreateNewUser:
    def __init__(
            self, user_repository: AbstractUserRepository
    ) -> None:
        self.user_repository = user_repository

    def execute(self, name: str, status: UserStatus):
        user = User(
            name=name,
            status=status,
        )
        self.user_repository.add(user)
