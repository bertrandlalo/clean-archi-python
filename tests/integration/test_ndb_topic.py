from datetime import datetime
from time import sleep

from google.cloud import ndb

from adapters.datastore.ndb_topic_repository import NDBTopicRepository
from adapters.datastore.ndb_user_repository import NDBUserRepository
from domain.ports import Topic, User

now = datetime.utcnow()
topic = Topic(topic_name="Antarctique", created_date=now, author_uuid="pat2b")


def test_can_add_topic():
    client = ndb.Client()
    with client.context():
        ndb_topic_repository = NDBTopicRepository()
        number_users_before_add = len(ndb_topic_repository.get_all())
        ndb_topic_repository.add(topic)
        sleep(0.5)  # store emulator needs some time
        assert len(ndb_topic_repository.get_all()) == number_users_before_add + 1


def test_can_get_topic():
    client = ndb.Client()
    with client.context():
        topic_repo = NDBTopicRepository()

        topic_from_ndb = topic_repo.get(topic.id)
        assert topic_from_ndb.author_uuid == topic.author_uuid
        assert topic_from_ndb.id == topic.id
        assert topic_from_ndb.topic_name == topic.topic_name


def test_can_get_all_topics():
    client = ndb.Client()
    with client.context():
        topic_repo = NDBTopicRepository()
        all_topics = topic_repo.get_all()
        assert type(all_topics) == list
        assert len(all_topics) > 0
        for topic in all_topics:
            assert type(topic) == Topic


def test_can_get_all_topics_and_authors():
    client = ndb.Client()
    with client.context():
        repo_topic = NDBTopicRepository()
        repo_user = NDBUserRepository()

        my_user = User(name='nathan malnoury', status='active')
        repo_user.add(my_user)

        my_topic = Topic(topic_name='ant', author_uuid=my_user.id)
        repo_topic.add(my_topic)

        async_operation = repo_topic.async_get_all_topics_and_authors()
        res = async_operation.result()
        print(res)
