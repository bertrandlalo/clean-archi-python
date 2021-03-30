from datetime import datetime

from google.cloud import ndb

from adapters.datastore.ndb_topic_repository import NDBTopicRepository
from adapters.datastore.ndb_user_repository import NDBUserRepository
from domain.ports import User, Topic

now = datetime.utcnow()
topic = Topic(topic_name="Antarctique", created_date=now, author_uuid="pat2b")


def test_can_add_topic():
    client = ndb.Client()
    with client.context():
        ndb_topic_repository = NDBTopicRepository()
        number_users_before_add = len(ndb_topic_repository.topics)
        ndb_topic_repository.add(topic)
        assert len(ndb_topic_repository.topics) == number_users_before_add + 1


def test_can_get_topic():
    client = ndb.Client()
    with client.context():
        topic_repo = NDBTopicRepository()

        topic_from_ndb = topic_repo.get(topic.id)
        assert topic_from_ndb.author_uuid == topic.author_uuid
        assert topic_from_ndb.id == topic.id
        assert topic_from_ndb.topic_name == topic.topic_name


def test_can_get_all_users():
    client = ndb.Client()
    with client.context():
        all_users = NDBUserRepository().users
        assert type(all_users) == list
        assert len(all_users) > 0
        for user in all_users:
            assert type(user) == User
