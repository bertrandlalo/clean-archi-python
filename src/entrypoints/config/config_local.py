from google.cloud import ndb
from adapters.datastore.ndb_user_repository import NDBUserRepository


class LocalConfig:
    def __init__(self):
        self.user_repo = NDBUserRepository(project_id='clean-experquiz')
        self.has_middleware = True

    @staticmethod
    def wsgi_middleware(wsgi_app):
        print("middleware started")
        def middleware(environ, start_response):
            client = ndb.Client()
            with client.context():
                return wsgi_app(environ, start_response)
        return middleware

