from domain.ports.user import User
from domain.ports.user.user_repository import InMemoryUserRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.get_all_users import GetAllUsers


def test_create_new_user():
    uuid_gen = CustomUuid()
    user_repository = InMemoryUserRepository(uuid_generator=uuid_gen)

    get_all_users = GetAllUsers(user_repository)
    user_repository.users = [User(uuid="pat_uuid", name="patrice", status="active")]
    actual_users = get_all_users.execute()
    assert actual_users == [User(uuid="pat_uuid", name="patrice", status="active")]
