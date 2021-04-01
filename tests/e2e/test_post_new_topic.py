from pathlib import Path
from flask import json
import pytest

from entrypoints.server import Config, make_app
from adapters.csv_user_repository import CsvUserRepository

from src.domain.ports.topic_repository import InMemoryTopicRepository

csv_path = Path("data") / "user_repo"
user_repo = CsvUserRepository(csv_path)
topic_repo = InMemoryTopicRepository()
config = Config(user_repo, topic_repo)


@pytest.fixture
def client():
    app = make_app(config)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_post_new_topic(client):
    rv = client.post(
        "/topic",
        data={
            "topic_text": "Antarctique",
            "status": "active",
            "topic_short": "ANT",
            "title": "Antarctique initiation",
            "description": "L'Antarctique, parfois appelé « le Continent Austral » ou « le Continent Blanc », est le continent le plus méridional de la Terre. Situé autour du pôle Sud, il est entouré des océans Atlantique, Indien et Pacifique et des mers de Ross et de Weddel",
        },
    )
    assert json.loads(rv.data) == "ok!"
