from adapters.ndb_topic_repository import NDBTopicRepository, flush_all_topics
from domain.models.topic import Topic
from google.cloud import ndb
from helpers.clock import CustomClock

client = ndb.Client()
clock = CustomClock()
topic = Topic(topic_name="Antarctique", author_uuid="pat2b", uuid="antarctique", created_date=clock.get_now())

with client.context():
    flush_all_topics()


def test_can_add_topic():
    with client.context():
        ndb_topic_repository = NDBTopicRepository()
        number_users_before_add = len(ndb_topic_repository.get_all())
        ndb_topic_repository.add(topic)
        assert len(ndb_topic_repository.get_all()) == number_users_before_add + 1


def test_can_get_topic():
    with client.context():
        topic_repo = NDBTopicRepository()
        topic_from_ndb = topic_repo.get(topic.uuid)
        assert topic_from_ndb == topic


def test_can_get_all_topics():
    with client.context():
        topic_repo = NDBTopicRepository()
        all_topics = topic_repo.get_all()
        assert all_topics == [topic]
