from domain.ports import User, Topic
from domain.ports.topic.topic_repository import InMemoryTopicRepository
from domain.ports.uuid import CustomUuid
from domain.use_cases.create_new_topic import CreateNewTopic


def test_create_new_topic():
    uuid_topic, uuid_user = 'topic_uuid', 'topic_user'
    topic_name = "My first topic"
    uuid = CustomUuid()
    uuid.set_next_uuid(uuid_topic)
    topic_repo = InMemoryTopicRepository(uuid_generator=uuid)
    user = User(first_name='patrice', last_name='bertrand', uuid=uuid_user)
    create_new_topic = CreateNewTopic(topic_repository=topic_repo)
    create_new_topic.execute(topic_name=topic_name, user=user)

    created_topic = topic_repo.topics[0]
    assert isinstance(created_topic, Topic), 'wrong type'
    assert created_topic.topic_name == topic_name, 'wrong name'
    assert created_topic.uuid == uuid_topic, "wrong uuid"
    assert created_topic.author == user, "wrong user"
