import binascii
from typing import List, Any

from google.cloud import ndb
from google.cloud.ndb import tasklet

from adapters.datastore.topic_ndb import TopicNDB
from domain.ports import Topic, User
from domain.ports.topic.topic_repository import AbstractTopicRepository
from domain.ports.user.user_repository import AbstractUserRepository


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

    def get_all(self) -> List[Topic]:
        topics_ndb: List[TopicNDB] = TopicNDB.query().fetch()
        return [top.to_topic() for top in topics_ndb]

    @tasklet
    def async_get_topic_and_user(self, topic_uuid, user_repo: AbstractUserRepository) -> (Topic, User):
        topic_ndb: TopicNDB = yield ndb.Key(urlsafe=topic_uuid).get_async()
        topic = topic_ndb.to_topic()
        user_key = topic.author_uuid
        try:
            user = user_repo.get(uuid=user_key)
            return topic, user
        except binascii.Error:
            print('could not retrieve user')

    @tasklet
    def async_get_all_topics_and_authors(self, user_repo: AbstractUserRepository):
        all_keys = yield TopicNDB.query().fetch_async(keys_only=True)
        all_keys = [key.urlsafe().decode() for key in all_keys]
        print(all_keys)
        futures = []
        for key in all_keys:
            futures.append(
                self.async_get_topic_and_user(topic_uuid=key, user_repo=user_repo)
            )
        yield futures
