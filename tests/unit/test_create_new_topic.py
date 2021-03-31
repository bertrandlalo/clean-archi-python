from src.domain.ports.user import User
from src.domain.ports.topic_repository import InMemoryTopicRepository
from src.domain.ports.user_repository import InMemoryUserRepository
from src.domain.use_cases.create_new_topic import CreateNewTopic
from src.domain.use_cases.create_new_user import CreateNewUser

from src.domain.ports.topic import Topic
from src.domain.ports.uuid import CustomUuid


def test_create_new_topic():
    topic_repository = InMemoryTopicRepository()
    uuid = CustomUuid()
    create_new_topic = CreateNewTopic(topic_repository, uuid)
    uuid.set_next_uuid("Antarctique")

    # create the author
    user_repository = InMemoryUserRepository()
    author = CreateNewUser(user_repository, uuid)
    uuid.set_next_uuid("antarc_author_uuid")
    author.execute(name="antarc_author", status="active")
    create_new_topic.execute(topic_text="Antarctique",
                             status="active",
                             topic_short= "ANT",
                             title= "Antarctique initiation",
                             description="Antarctique, parfois appelé",
                             author=User(uuid="antarc_author_uuid", name="antarc_author", status="active"))
    assert len(topic_repository.topics) == 1

    expected_topic = Topic(

        uuid="Antarctique",
        topic_text= "Antarctique",
        status="active",
        topic_short="ANT",
        title="Antarctique initiation",
        description="Antarctique, parfois appelé",
        author=User(uuid="antarc_author_uuid", name="antarc_author", status="active"))

    assert topic_repository.topics[0] == expected_topic