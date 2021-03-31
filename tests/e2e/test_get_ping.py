import pytest
from flask import json

from entrypoints.config import ndb_config
from entrypoints.server import make_app

config = ndb_config


@pytest.fixture
def client():
    app = make_app(config)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_ping(client):
    rv = client.get("/ping")
    assert json.loads(rv.data) == "pong!"


def test_get_users(client):
    rv = client.get("/users")
    rv_json = rv.get_json()
    assert type(rv_json) == list
