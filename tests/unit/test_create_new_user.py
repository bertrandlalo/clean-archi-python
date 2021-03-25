from domain.ports.model import User
from domain.ports.user_repository import InMemoryUserRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.create_new_user import CreateNewUser


def test_create_new_user():
    uuid = CustomUuid()
    uuid.set_next_uuid("pat_uuid")
    user_repository = InMemoryUserRepository(uuid_generator=uuid)
    create_new_user = CreateNewUser(user_repository=user_repository)
    create_new_user.execute(first_name="patrice", last_name="bertrand")
    expected_user = User(first_name="patrice", last_name="bertrand", uuid="pat_uuid")
    assert user_repository.users == [expected_user]
