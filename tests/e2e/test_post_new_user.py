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


def test_post_new_user(client):
    rv = client.post("/user", data={"name": "patrice", "status": "active"})
    assert json.loads(rv.data) == "ok!"
