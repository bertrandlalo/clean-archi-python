import csv
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from domain.ports import Topic
from domain.ports.topic.topic_repository import AbstractTopicRepository
from domain.ports.uuid import AbstractUuid


def mkdir_if_relevant(path: Path):
    if not os.path.isdir(path):
        os.mkdir(path)


def writerow(csv_path: Path, row: List):
    with csv_path.open("a") as f:
        writer = csv.writer(f)
        writer.writerow(row)


class CsvTopicRepository(AbstractTopicRepository):
    _topics: List[Topic]

    def __init__(self, csv_path: Path, uuid_generator: AbstractUuid) -> None:
        self._topics = []
        self.csv_path = csv_path
        self.uuid_generator = uuid_generator
        csv_columns = ["uuid", "author_uuid", "topic_name", "created_date"]
        if os.path.isfile(self.csv_path):
            self._from_csv()
        else:
            mkdir_if_relevant(self.csv_path.parent)
            writerow(self.csv_path, csv_columns)

    def add(self, topic: Topic):
        topic_id = self.uuid_generator.make()
        topic.set_id(topic_id)
        self.topics.append(topic)
        writerow(
            self.csv_path,
            [
                topic.uuid,
                topic.author_uuid,
                topic.topic_name,
                topic.created_date.timestamp(),
            ],
        )

    def _from_csv(self):
        self._topics = []
        with self.csv_path.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._topics.append(
                    Topic(
                        uuid=row.get('uuid'),
                        author_uuid=row.get('author_uuid'),
                        topic_name=row.get('topic_name'),
                        created_date=datetime.utcfromtimestamp(float(row.get('created_date')))
                    )
                )

    def get(self, uuid: str) -> Optional[Topic]:
        return [topic for topic in self.topics if topic.uuid == uuid].pop()

    def get_all_from_user(self, user_uuid: str) -> List[Topic]:
        return [topic for topic in self.topics if topic.author_uuid == user_uuid]

    @property
    def topics(self) -> List[Topic]:
        return self._topics
