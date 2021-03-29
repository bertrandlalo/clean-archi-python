from datetime import datetime

from domain.ports import User, Topic
from domain.ports.topic.topic_repository import AbstractTopicRepository
from domain.ports.uuid import AbstractUuid


class CreateNewTopic:
    def __init__(self, topic_repository: AbstractTopicRepository, uuid_generator: AbstractUuid):
        self.uuid_generator = uuid_generator
        self.topic_repository = topic_repository

    def execute(self, user: User, topic_name: str):
        new_base = Topic(topic_name=topic_name, author=user, created_date=datetime.utcnow())
        new_base.set_id(self.uuid_generator.make())
        self.topic_repository.add(new_base)
