from entrypoints.config.config import Config
from google.cloud import ndb

from adapters.ndb_topic_repository import NDBTopicRepository
from adapters.ndb_user_repository import NDBUserRepository


def wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        client = ndb.Client()
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


ndb_config = Config(
    user_repository=NDBUserRepository(),
    topic_repository=NDBTopicRepository(),
    # has_middleware=True,
    # wsgi_middleware=wsgi_middleware,
)
