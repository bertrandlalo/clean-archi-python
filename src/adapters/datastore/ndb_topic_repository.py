from typing import List, Any

from google.cloud import ndb

from adapters.datastore.topic_ndb import TopicNDB
from domain.ports import Topic
from domain.ports.topic.topic_repository import AbstractTopicRepository


class NDBTopicRepository(AbstractTopicRepository):

    def add(self, topic: Topic):
        topic_ndb = TopicNDB.from_topic(topic)
        topic_ndb.put()
        topic.set_id(topic_ndb.id)

    def get(self, uuid: Any) -> Topic:
        topic_ndb: TopicNDB = ndb.Key(urlsafe=uuid).get()
        return topic_ndb.to_topic()

    def get_all_from_user(self, user_uuid: str) -> List[Topic]:
        list_topic_ndb: List[TopicNDB] = TopicNDB.query(TopicNDB.author_uuid == user_uuid).fetch()
        return [topic_ndb.to_topic() for topic_ndb in list_topic_ndb]

    @property
    def topics(self) -> List[Topic]:
        return TopicNDB.query().fetch()
