import csv
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from domain.models.topic import Topic
from domain.ports.topic_repository import AbstractTopicRepository


def mkdir_if_relevant(path: Path):
    if not os.path.isdir(path):
        os.mkdir(path)


def writerow(csv_path: Path, row: List):
    with csv_path.open("a") as f:
        writer = csv.writer(f)
        writer.writerow(row)


class CsvTopicRepository(AbstractTopicRepository):
    _topics: List[Topic]

    def __init__(self, csv_path: Path) -> None:
        self._topics = []
        self.csv_path = csv_path
        csv_columns = ["uuid", "author_uuid", "topic_name", "created_date"]
        if os.path.isfile(self.csv_path):
            self._from_csv()
        else:
            mkdir_if_relevant(self.csv_path.parent)
            writerow(self.csv_path, csv_columns)

    def add(self, topic: Topic):
        self._topics.append(topic)
        writerow(
            self.csv_path,
            [
                topic.uuid,
                topic.author_uuid,
                topic.topic_name,
                topic.created_date,
            ],
        )

    def _from_csv(self):
        self._topics = []
        with self.csv_path.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._topics.append(Topic(**row))

    def get(self, uuid: str) -> Optional[Topic]:
        return [topic for topic in self._topics if topic.uuid == uuid].pop()

    def get_all_from_user(self, user_uuid: str) -> List[Topic]:
        return [topic for topic in self._topics if topic.author_uuid == user_uuid]

    def get_all(self) -> List[Topic]:
        return self._topics
