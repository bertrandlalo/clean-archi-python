from datetime import datetime
from domain.models.topic import Topic

from domain.models.user import User
from domain.ports.topic_repository import AbstractTopicRepository
from domain.ports.uuid import AbstractUuid
from helpers.clock import AbstractClock


class CreateNewTopic:
    def __init__(
        self,
        topic_repository: AbstractTopicRepository,
        uuid: AbstractUuid,
        clock: AbstractClock,
    ) -> None:
        self.topic_repository = topic_repository
        self.uuid = uuid
        self.clock = clock

    def execute(self, user: User, topic_name: str):
        new_base = Topic(
            topic_name=topic_name,
            author_uuid=user.uuid,
            created_date=self.clock.get_now(),
            uuid=self.uuid.make(),
        )
        self.topic_repository.add(new_base)
