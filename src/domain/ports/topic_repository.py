import abc
from typing import List
from domain.ports.topic import Topic


class AbstractTopicRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, topic: Topic):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self) -> List[Topic]:
        raise NotImplementedError


class InMemoryTopicRepository(AbstractTopicRepository):
    _topics: List[Topic]

    def __init__(self):
        self._topics = []

    def add(self, topic: Topic):
        self._topics.append(topic)

    def get_all(self) -> List[Topic]:
        return self._topics

    # For test purposes only
    @property
    def topics(self) -> List[Topic]:
        return self._topics

    @topics.setter
    def topics(self, topics: List[Topic]):
        self._topics = topics