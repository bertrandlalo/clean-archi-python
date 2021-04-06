from domain.models.user import User
from domain.ports.user_repository import InMemoryUserRepository
from domain.use_cases.get_all_users import GetAllUsers


def test_create_new_user():
    user_repository = InMemoryUserRepository()
    get_all_users = GetAllUsers(user_repository)
    user_repository.users = [User(uuid="pat_uuid", name="patrice", status="active")]
    actual_users = get_all_users.execute()
    assert actual_users == [User(uuid="pat_uuid", name="patrice", status="active")]
