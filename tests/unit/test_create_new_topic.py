import pytest

from domain.models.topic import Topic
from domain.models.user import User
from domain.ports.topic_repository import InMemoryTopicRepository
from domain.ports.user_repository import InMemoryUserRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.create_new_topic import CreateNewTopic, UserDoesNotExist
from helpers.clock import CustomClock, DateStr

uuid_topic, uuid_user = "topic_uuid", "user_uuid"
topic_name = "My first topic"
created_date = DateStr("2021-05-15:00:00:00.1")


def test_create_new_topic_when_user_does_not_exist():
    uuid = CustomUuid()
    clock = CustomClock()
    uuid.set_next_uuid(uuid_topic)
    clock.set_next_date(created_date)
    topic_repo = InMemoryTopicRepository()
    user_repo = InMemoryUserRepository()
    user = User(name="patrice", status="active", uuid=uuid_user)

    create_new_topic = CreateNewTopic(
        topic_repository=topic_repo, uuid=uuid, clock=clock, user_repository=user_repo
    )

    with pytest.raises(UserDoesNotExist):
        create_new_topic.execute(topic_name=topic_name, user=user)


def test_create_new_topic_when_user_exists():
    uuid = CustomUuid()
    clock = CustomClock()
    uuid.set_next_uuid(uuid_topic)
    clock.set_next_date(created_date)
    topic_repo = InMemoryTopicRepository()
    user_repo = InMemoryUserRepository()
    user = User(name="patrice", status="active", uuid=uuid_user)

    user_repo.users = [user]

    create_new_topic = CreateNewTopic(
        topic_repository=topic_repo, uuid=uuid, clock=clock, user_repository=user_repo
    )
    create_new_topic.execute(topic_name=topic_name, user=user)
    assert len(topic_repo.topics) == 1
    assert topic_repo.topics[0] == Topic(
        author_uuid=uuid_user,
        topic_name=topic_name,
        uuid=uuid_topic,
        created_date=created_date,
    )


# def test_create_new_topic_when_user_exists():
#     uuid_topic, uuid_user = "topic_uuid", "user_uuid"
#     topic_name = "My first topic"
#     uuid = CustomUuid()
#     clock = CustomClock()
#     uuid.set_next_uuid(uuid_topic)
#     created_date = DateStr("2021-05-15:00:00:00.1")
#     clock.set_next_date(created_date)
#     topic_repo = InMemoryTopicRepository()
#     user = User(name="patrice", status="active", uuid=uuid_user)
#     create_new_topic = CreateNewTopic(
#         topic_repository=topic_repo, uuid=uuid, clock=clock
#     )
#     create_new_topic.execute(topic_name=topic_name, user=user)
#     assert len(topic_repo.topics) == 1
#     assert topic_repo.topics[0] == Topic(
#         author_uuid=uuid_user,
#         topic_name=topic_name,
#         uuid=uuid_topic,
#         created_date=created_date,
#     )

# assert isinstance(created_topic, Topic), "wrong type"
# assert created_topic.topic_name == topic_name, "wrong name"
# assert created_topic.uuid == uuid_topic, "wrong uuid"
# assert created_topic.author_uuid == user.uuid, "wrong user"
