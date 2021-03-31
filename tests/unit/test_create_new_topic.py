import datetime
from domain.models.user import User
from domain.models.topic import Topic
from domain.ports.topic_repository import InMemoryTopicRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.create_new_topic import CreateNewTopic
from helpers.clock import CustomClock, DateStr


def test_create_new_topic():
    uuid_topic, uuid_user = "topic_uuid", "user_uuid"
    topic_name = "My first topic"
    uuid = CustomUuid()
    uuid.set_next_uuid(uuid_topic)
    topic_repo = InMemoryTopicRepository()

    user = User(name="patrice", status="active", uuid=uuid_user)
    clock = CustomClock()
    created_date = DateStr("2021-01-01T12:00:00.0")
    clock.set_next_date(created_date)
    create_new_topic = CreateNewTopic(
        topic_repository=topic_repo, uuid=uuid, clock=clock
    )
    create_new_topic.execute(topic_name=topic_name, user=user)
    assert len(topic_repo._topics) == 1
    assert topic_repo._topics[0] == Topic(
        uuid=uuid_topic,
        topic_name=topic_name,
        author_uuid=uuid_user,
        created_date=created_date,
    )

    # created_topic = topic_repo.get_all()[0]
    # assert isinstance(created_topic, Topic), "wrong type"
    # assert created_topic.topic_name == topic_name, "wrong name"
    # assert created_topic.uuid == uuid_topic, "wrong uuid"
    # assert created_topic.author_uuid == user.uuid, "wrong user"
