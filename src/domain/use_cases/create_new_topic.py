from domain.models.topic import Topic
from domain.models.user import User
from domain.ports.topic_repository import AbstractTopicRepository
from domain.ports.user_repository import AbstractUserRepository
from domain.ports.uuid import AbstractUuid
from helpers.clock import AbstractClock, from_datetime


class UserDoesNotExist(Exception):
    pass


class CreateNewTopic:
    def __init__(
        self,
        topic_repository: AbstractTopicRepository,
        user_repository: AbstractUserRepository,
        uuid: AbstractUuid,
        clock: AbstractClock,
    ):
        self.topic_repository = topic_repository
        self.user_repository = user_repository
        self.uuid = uuid
        self.clock = clock

    def execute(self, user: User, topic_name: str):
        if not self.user_repository.get(user.uuid):
            raise UserDoesNotExist("user does not exist in repo")
        new_base = Topic(
            topic_name=topic_name,
            author_uuid=user.uuid,
            created_date=self.clock.get_now(),
            uuid=self.uuid.make(),
        )
        self.topic_repository.add(new_base)
