from typing import List, Any

from domain.models.topic import Topic
from domain.ports.topic_repository import AbstractTopicRepository
from google.cloud import ndb


class NDBTopicRepository(AbstractTopicRepository):
    def add(self, topic: Topic):
        topic_ndb = TopicNDB(author_uuid=topic.author_uuid,
                             topic_name=topic.topic_name,
                             created_date=topic.created_date,
                             uuid=topic.uuid, id=topic.uuid)
        topic_ndb.put()

    def get(self, uuid: Any) -> Topic:
        topic_ndb: TopicNDB = TopicNDB.get_by_id(uuid)
        return topic_ndb.to_topic()

    def get_all_from_user(self, user_uuid: str) -> List[Topic]:
        list_topic_ndb: List[TopicNDB] = TopicNDB.query(TopicNDB.author_uuid == user_uuid).fetch()
        return [topic_ndb.to_topic() for topic_ndb in list_topic_ndb]

    def get_all(self) -> List[Topic]:
        topics_ndb: List[TopicNDB] = TopicNDB.query().fetch()
        return [top.to_topic() for top in topics_ndb]


class TopicNDB(ndb.Model):
    author_uuid = ndb.StringProperty()
    topic_name = ndb.StringProperty()
    uuid = ndb.StringProperty()
    created_date = ndb.StringProperty()  # contains a DateStr

    def to_topic(self) -> Topic:
        return Topic(author_uuid=self.author_uuid,
                     topic_name=self.topic_name,
                     created_date=self.created_date,
                     uuid=self.uuid)


def flush_all_topics():
    ndb.delete_multi(TopicNDB.query().fetch(keys_only=True))
