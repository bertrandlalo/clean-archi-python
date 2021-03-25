from domain.ports import AbstractUserRepository


class ListUsers:
    def __init__(self, user_repository: AbstractUserRepository) -> None:
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.users
