from domain.ports.user import User
from domain.ports.topic_repository import InMemoryTopicRepository
from domain.use_cases.create_new_topic import CreateNewTopic

from src.domain.ports.topic import Topic
from src.domain.ports.uuid import CustomUuid


def test_create_new_topic():
    topic_repository = InMemoryTopicRepository()
    uuid = CustomUuid()
    create_new_topic = CreateNewTopic(topic_repository, uuid)
    uuid.set_next_uuid("Antarctique")
    create_new_topic.execute(topic_text="Antarctique",
                             status="active",
                             topic_short= "ANT",
                             title= "Antarctique initiation",
                             description="Antarctique, parfois appelé")
    assert len(topic_repository.topics) == 1

    expected_topic = Topic(
        uuid="Antarctique",
        topic_text= "Antarctique",
        status="active",
        topic_short="ANT",
        title="Antarctique initiation",
        description="Antarctique, parfois appelé")

    assert topic_repository.topics[0] == expected_topic