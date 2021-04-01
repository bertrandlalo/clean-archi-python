from pathlib import Path
from flask import json
import pytest

from adapters.csv_user_repository import CsvUserRepository
from entrypoints.server import Config, make_app
from helpers.csv import reset_file_from_path

from src.domain.ports.topic_repository import InMemoryTopicRepository
from tests.utils.write_csv_file import write_csv_file

csv_path = Path("data") / "user_repo"
write_csv_file(
    csv_path,
    header=["uuid", "name", "status"],
    rows=[["pat_uuid", "patrice", "deleted"]],
)
user_repo = CsvUserRepository(csv_path)
topic_repo = InMemoryTopicRepository()
config = Config(user_repo, topic_repo)


@pytest.fixture
def client():
    app = make_app(config)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_users(client):
    rv = client.get("/users")
    assert json.loads(rv.data) == [
        {"name": "patrice", "status": "deleted", "uuid": "pat_uuid"}
    ]
