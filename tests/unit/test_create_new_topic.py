from domain.ports.user import User
from domain.ports.topic_repository import InMemoryTopicRepository
from domain.use_cases.create_new_topic import CreateNewTopic

from domain.ports.topic import Topic
from domain.ports.uuid import CustomUuid


def test_create_new_topic_from_existing_user():
    topic_repository = InMemoryTopicRepository()
    topic_uuid = CustomUuid()
    topic_uuid.set_next_uuid("Antarctique")
    create_new_topic = CreateNewTopic(topic_repository, topic_uuid)

    # create the author
    author = User(uuid="antarc_author_uuid", name="antarc_author", status="active")
    create_new_topic.execute(
        topic_text="Antarctique",
        status="active",
        topic_short="ANT",
        title="Antarctique initiation",
        description="Antarctique, parfois appelé",
        author=author,
    )
    assert len(topic_repository.topics) == 1

    expected_topic = Topic(
        uuid="Antarctique",
        topic_text="Antarctique",
        status="active",
        topic_short="ANT",
        title="Antarctique initiation",
        description="Antarctique, parfois appelé",
        author=author,
    )

    assert topic_repository.topics[0] == expected_topic