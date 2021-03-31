import csv
from datetime import datetime
from pathlib import Path

from adapters.csv_topic_repository import CsvTopicRepository
from domain.ports import Topic
from domain.ports.uuid import CustomUuid
from helpers.csv import reset_file_from_path

csv_path = Path("tests/integration/data") / "topic_repo.csv"

created_date = datetime.utcnow()
topic_example = Topic(topic_name="Antarctique", author_uuid="pat2b", created_date=created_date)


def test_can_add_topic():
    reset_file_from_path(csv_path)
    uuid = CustomUuid()
    uuid.set_next_uuid("ant")
    csv_user_repository = CsvTopicRepository(csv_path=csv_path, uuid_generator=uuid)
    csv_user_repository.add(topic_example)
    with csv_path.open("r") as f:
        reader = csv.DictReader(f)
        assert list(reader)[0] == dict(
            uuid='ant', author_uuid="pat2b", created_date=str(created_date.timestamp()), topic_name="Antarctique",
        )


def test_can_get_topic_if_exists():
    reset_file_from_path(csv_path)
    uuid = CustomUuid()
    uuid.set_next_uuid("ant")
    csv_topic_repository = CsvTopicRepository(csv_path=csv_path, uuid_generator=uuid)
    csv_topic_repository.add(topic_example)
    assert csv_topic_repository.get(uuid="ant") == topic_example


def test_data_persistence():
    reset_file_from_path(csv_path)
    uuid = CustomUuid()
    uuid.set_next_uuid('ant')
    csv_topic_repository = CsvTopicRepository(csv_path=csv_path, uuid_generator=uuid)
    csv_topic_repository.add(topic_example)

    second_repo = CsvTopicRepository(csv_path, uuid_generator=uuid)
    assert second_repo.get('ant')
