from domain.ports.topic import Topic, TopicStatus
from domain.ports.topic_repository import AbstractTopicRepository

# from domain.ports.uuid import AbstractUuid
from src.domain.ports.uuid import AbstractUuid


class CreateNewTopic:
    def __init__(
            self,
            topic_repository: AbstractTopicRepository,
            uuid=AbstractUuid
    ) -> None:
        self.topic_repository = topic_repository
        self.uuid = uuid


    def execute(self,
                topic_text: str,
                status: TopicStatus,
                topic_short: str,
                title: str,
                description: str):

        topic = Topic(
            uuid=self.uuid.make(),
            topic_text=topic_text,
            status='active',
            topic_short=topic_text[:3],
            title=title,
            description=description

        )
        self.topic_repository.add(topic)
topic_text: str



