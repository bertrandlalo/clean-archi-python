from typing import List, Any

from domain.ports import Topic
from domain.ports.topic.topic_repository import AbstractTopicRepository
from domain.ports.user.user_repository import AbstractUserRepository


class GetAllTopicsOfUser:
    def __init__(
            self, user_repository: AbstractUserRepository,
            topic_repository: AbstractTopicRepository,
    ) -> None:
        self.topic_repository = topic_repository
        self.user_repository = user_repository

    def execute(self, user_uuid: Any) -> List[Topic]:
        return self.topic_repository.get_all_from_user(user_uuid)
