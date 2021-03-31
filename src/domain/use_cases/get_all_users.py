from domain.ports.user.user_repository import AbstractUserRepository


class GetAllUsers:
    def __init__(self, user_repository: AbstractUserRepository) -> None:
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.get_all()
