from datetime import datetime

from domain.ports import User, Topic
from domain.ports.topic.topic_repository import AbstractTopicRepository
from domain.ports.uuid import AbstractUuid


class CreateNewTopic:
    def __init__(self, topic_repository: AbstractTopicRepository):
        self.topic_repository = topic_repository

    def execute(self, user: User, topic_name: str):
        new_base = Topic(topic_name=topic_name, author_uuid=user.id)
        self.topic_repository.add(new_base)
