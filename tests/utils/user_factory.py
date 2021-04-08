from domain.models.user import User, UserStatus

default_name = "patrice"
default_mail = "pat@gmail.com"
default_password = "patb2"
default_status: UserStatus = "active"
default_uuid = "pat_uuid"


def make_user(
    name: str = default_name,
    mail: str = default_mail,
    password: str = default_password,
    status: UserStatus = default_status,
    uuid: str = default_uuid,
) -> User:
    return User(name, status, uuid=uuid)
