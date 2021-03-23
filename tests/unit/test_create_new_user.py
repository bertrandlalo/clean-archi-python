from src.domain.ports.model import User
from src.domain.ports.user_repository import InMemoryUserRepository
from src.domain.ports.uuid import CustomUuid
from src.domain.use_cases.create_new_user import CreateNewUser


def test_create_new_user():
    user_repository = InMemoryUserRepository()
    uuid = CustomUuid()
    uuid.set_next_uuid("pat_uuid")
    create_new_user = CreateNewUser(user_repository=user_repository, uuid=uuid)
    create_new_user.execute(first_name="patrice", last_name="bertrand")
    expected_user = User(first_name="patrice", last_name="bertrand", uuid="pat_uuid")
    assert user_repository.users == [expected_user]