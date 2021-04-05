from pathlib import Path
from flask import json
import pytest
from adapters.csv_topic_repository import CsvTopicRepository

from adapters.csv_user_repository import CsvUserRepository
from entrypoints.server import make_app
from entrypoints.config.config import Config

from tests.utils.write_csv_file import write_csv_file

user_csv_path = Path("data") / "user_repo"
write_csv_file(
    user_csv_path,
    header=["uuid", "name", "status"],
    rows=[["pat_uuid", "patrice", "deleted"]],
)
user_repo = CsvUserRepository(user_csv_path)
topic_repo = CsvTopicRepository(Path("data") / "topic_repo")
config = Config(user_repository=user_repo, topic_repository=topic_repo)


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