from src.domain.ports.user_repository import AbstractUserRepository
from src.domain.ports.model import User


class AddUser:
    def __init__(self, user_repository: AbstractUserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user: User):
        self.user_repository.add(user)
