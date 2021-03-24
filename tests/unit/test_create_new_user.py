from domain.ports.user import User
from domain.ports.user_repository import AbstractUserRepository, InMemoryUserRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.create_new_user import CreateNewUser


def test_create_new_user():
    user_repository = InMemoryUserRepository()
    uuid = CustomUuid()
    create_new_user = CreateNewUser(user_repository, uuid)
    uuid.set_next_uuid("pat_uuid")
    create_new_user.execute(name="patrice", status="active")
    assert len(user_repository.users) == 1
    expected_user = User(uuid="pat_uuid", name="patrice", status="active")
    assert user_repository.users == [expected_user]