from domain.models import commands
from domain.models.events import UserCreated
from tests.utils.spy_on_event import spy_on_event
from typing import List
import pytest

from domain.models.user import User
from domain.ports.user_repository import InMemoryUserRepository
from domain.ports.uuid import CustomUuid
from domain.services.domain_message_bus import InMemoryDomainMessageBus
from domain.use_cases.create_new_user import CreateNewUser, UserNameAlreadyExists


# def test_create_new_user():
#     uuid = CustomUuid()
#     user_repository = InMemoryUserRepository()
#     create_new_user = CreateNewUser(user_repository, uuid)
#     uuid.set_next_uuid("pat_uuid")
#     create_new_user.execute(name="patrice", status="active")
#     assert len(user_repository.users) == 1
#     expected_user = User(uuid="pat_uuid", name="patrice", status="active")
#     assert user_repository.users == [expected_user]


# def test_create_new_user_if_name_already_exists():
#     uuid = CustomUuid()
#     user_repository = InMemoryUserRepository([User("patrice", "active", "pat_uuid")])
#     create_new_user = CreateNewUser(user_repository, uuid)
#     with pytest.raises(UserNameAlreadyExists):
#         create_new_user.execute(name="patrice", status="active")
#     assert len(user_repository.users) == 1


def test_create_new_user_if_name_already_exists():
    uuid = CustomUuid()
    user_repository = InMemoryUserRepository([User("patrice", "active", "pat_uuid")])
    bus = InMemoryDomainMessageBus()
    create_new_user = CreateNewUser(user_repository, uuid, bus=bus)
    published_events = spy_on_event(bus, UserNameAlreadyExists)
    # create_new_user.execute(name="patrice")
    create_new_user.execute(commands.CreateNewUser(name="patrice"))
    assert len(user_repository.users) == 1
    assert len(published_events) == 1
    assert published_events[0].status == "active"


def test_create_new_user():
    uuid = CustomUuid()
    user_repository = InMemoryUserRepository()
    bus = InMemoryDomainMessageBus()
    create_new_user = CreateNewUser(user_repository, uuid, bus)
    published_events = spy_on_event(bus, UserCreated)
    uuid.set_next_uuid("pat_uuid")
    # create_new_user.execute(name="patrice")
    create_new_user.execute(commands.CreateNewUser(name="patrice"))

    assert len(user_repository.users) == 1
    assert len(published_events) == 1
    assert user_repository.users == [
        User(uuid="pat_uuid", name="patrice", status="pending")
    ]
    assert published_events == [UserCreated(name="patrice")]