import abc
from typing import Any, List, Optional

from domain.models.topic import Topic
from domain.models.user import User


class AbstractTopicRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, topic: Topic):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: Any) -> Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_from_user(self, user_uuid: str) -> List[Topic]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self) -> List[Topic]:
        raise NotImplementedError


class InMemoryTopicRepository(AbstractTopicRepository):
    _topics: List[Topic]

    def __init__(self) -> None:
        self._topics = []

    def add(self, topic: Topic):
        self._topics.append(topic)

    def get(self, uuid: str) -> Optional[Topic]:
        for topic in self._topics:
            if topic.uuid == uuid:
                return topic

    def get_all_from_user(self, user_uuid: User) -> List[Topic]:
        return [topic for topic in self._topics if user_uuid == topic.author_uuid]

    def get_all(self) -> List[Topic]:
        return self._topics

    # For test purposes only
    @property
    def topics(self) -> List[Topic]:
        return self._topics

    @topics.setter
    def topics(self, topics: List[Topic]):
        self._topics = topics
