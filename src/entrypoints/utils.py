from google.cloud import ndb


def ndb_middleware(wsgi_app):
    def wrapper(environ, start_response):
        with ndb.Client().context():
            return wsgi_app(environ, start_response)

    return wrapper
