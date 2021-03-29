import abc
from typing import Any, List

from domain.ports import Topic
from domain.ports import User


class AbstractTopicRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, topic: Topic):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: Any) -> Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_from_user(self, user: User) -> List[Topic]:
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_async(self, uuid: Any):
    #     raise NotImplementedError

    @property
    @abc.abstractmethod
    def topics(self) -> List[Topic]:
        raise NotImplementedError


class InMemoryTopicRepository(AbstractTopicRepository):
    _topics: List[Topic]

    def __init__(self) -> None:
        self._topics = []

    def add(self, topic: Topic):
        self._topics.append(topic)

    def get(self, uuid: str) -> Topic:
        for topic in self._topics:
            if topic.uuid == uuid:
                return topic

    def get_all_from_user(self, user: User) -> List[Topic]:
        return [topic for topic in self._topics if user == topic.author]

    @property
    def topics(self) -> List[Topic]:
        return self._topics
