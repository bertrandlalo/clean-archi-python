from google.cloud import ndb

from adapters.datastore.ndb_user_repository import NDBUserRepository
from entrypoints.config.model import Config


def wsgi_middleware(wsgi_app):
    print("middleware started")

    def middleware(environ, start_response):
        client = ndb.Client()
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware




ndb_config = Config(
    user_repo=NDBUserRepository(),
    # topic_repo=NDBTopicRepository(project_id=PROJECT_ID),  # Todo : NDBTopicRepository
    topic_repo=None,
    has_middleware=True,
    wsgi_middleware=wsgi_middleware,
)
