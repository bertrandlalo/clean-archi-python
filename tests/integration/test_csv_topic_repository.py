import csv
from pathlib import Path

from adapters.csv_topic_repository import CsvTopicRepository
from domain.models.topic import Topic
from helpers.clock import DateStr
from helpers.csv import reset_file_from_path

csv_path = Path("tests/integration/data") / "topic_repo.csv"

topic_example = Topic(
    topic_name="Antarctique",
    author_uuid="pat2b",
    created_date=DateStr("2021-01-01T12:11:00.0"),
    uuid="ant",
)


def test_can_add_topic():
    reset_file_from_path(csv_path)
    csv_user_repository = CsvTopicRepository(csv_path=csv_path)
    csv_user_repository.add(topic_example)
    with csv_path.open("r") as f:
        reader = csv.DictReader(f)
        assert list(reader)[0] == dict(
            uuid="ant",
            author_uuid="pat2b",
            created_date=DateStr("2021-01-01T12:11:00.0"),
            topic_name="Antarctique",
        )


def test_can_get_topic_if_exists():
    reset_file_from_path(csv_path)
    csv_topic_repository = CsvTopicRepository(csv_path=csv_path)
    csv_topic_repository.add(topic_example)
    assert csv_topic_repository.get(uuid="ant") == topic_example


def test_data_persistence():
    reset_file_from_path(csv_path)
    csv_topic_repository = CsvTopicRepository(csv_path=csv_path)
    csv_topic_repository.add(topic_example)

    second_repo = CsvTopicRepository(csv_path)
    assert second_repo.get("ant")
