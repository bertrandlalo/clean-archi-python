from pathlib import Path
from flask import json
import pytest

from entrypoints.server import Config, make_app
from adapters.csv_user_repository import CsvUserRepository

csv_path = Path("data") / "user_repo"
user_repo = CsvUserRepository(csv_path)
config = Config(user_repo)


@pytest.fixture
def client():
    app = make_app(config)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_post_new_user(client):
    rv = client.post("/user", data={"name": "patrice", "status": "active"})
    assert json.loads(rv.data) == "ok!"
