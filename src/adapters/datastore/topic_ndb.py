from google.cloud import ndb

from domain.ports import Topic


class TopicNDB(ndb.Model):
    author_uuid = ndb.StringProperty()
    topic_name = ndb.StringProperty()
    created_date = ndb.DateProperty(auto_now_add=True)

    @staticmethod
    def from_topic(topic:Topic) -> 'TopicNDB':
        return TopicNDB(author_uuid=topic.author_uuid, topic_name=topic.topic_name, created_date=topic.created_date)

    def to_topic(self)->Topic:
        return Topic(author_uuid=self.author_uuid, topic_name=self.topic_name, created_date=self.created_date)
