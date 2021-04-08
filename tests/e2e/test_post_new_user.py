from pathlib import Path
from domain.models.events import EmailSentToWelcomeUser
from tests.utils.spy_on_event import spy_on_event
import pytest
from flask import json
from adapters.csv_topic_repository import CsvTopicRepository
from adapters.csv_user_repository import CsvUserRepository
from domain.ports.topic_repository import InMemoryTopicRepository
from domain.ports.user_repository import InMemoryUserRepository

from entrypoints.config.config import Config
from entrypoints.server import make_app

config = Config(
    user_repository=InMemoryUserRepository(),
    topic_repository=InMemoryTopicRepository(),
)


@pytest.fixture
def client():
    app = make_app(config)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_post_new_user(client):
    published_events = spy_on_event(config.bus, EmailSentToWelcomeUser)
    rv = client.post("/user", data={"name": "patrice"})
    assert rv.status == "200 OK"
    assert json.loads(rv.data) == {
        "name": "patrice",
    }
    assert len(published_events) == 1


def test_post_user_with_existing_name(client):
    rv = client.post("/user", data={"name": "patrice"})
    assert json.loads(rv.data) == {"name": "patrice", "status": "pending"}
