from domain.models.user import User
from domain.ports.user_repository import InMemoryUserRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.get_all_users import GetAllUsers


def test_get_all_users():
    user_repository = InMemoryUserRepository()
    user_repository.users = [User(uuid="pat_uuid", name="patrice", status="active")]
    get_all_users = GetAllUsers(user_repository)
    actual_users = get_all_users.execute()
    assert actual_users == [User(uuid="pat_uuid", name="patrice", status="active")]
