from pathlib import Path
import pytest
from flask import json
from adapters.csv_topic_repository import CsvTopicRepository
from adapters.csv_user_repository import CsvUserRepository

from entrypoints.config.config import Config
from entrypoints.server import make_app

config = Config(
    user_repository=CsvUserRepository(csv_path=Path("data") / "user_repo"),
    topic_repository=CsvTopicRepository(csv_path=Path("data") / "topic_repo"),
)


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
