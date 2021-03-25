import csv
import os
from pathlib import Path
from typing import List, Optional

from domain.ports.model import User
from domain.ports.user_repository import (
    AbstractUserRepository,
)


def mkdir_if_relevant(path: Path):
    if not os.path.isdir(path):
        os.mkdir(path)


def writerow(csv_path: Path, row: List):
    with csv_path.open("a") as f:
        writer = csv.writer(f)
        writer.writerow(row)


class CsvUserRepository(AbstractUserRepository):
    _users: List[User]

    def __init__(self, csv_path: Path) -> None:
        self._users = []
        self.csv_path = csv_path
        csv_columns = ["uuid", "first_name", "last_name"]  # User.__annotations__.keys()
        if os.path.isfile(self.csv_path):
            self._from_csv()
        else:
            mkdir_if_relevant(self.csv_path.parent)
            writerow(self.csv_path, csv_columns)

    def add(self, user: User):
        self._users.append(user)
        writerow(
            self.csv_path,
            [
                user.uuid,
                user.first_name,
                user.last_name,
            ],
        )

    def _from_csv(self) -> List[User]:
        self._users = []
        with self.csv_path.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._users.append(User(**row))

    def get(self, uuid: str) -> Optional[User]:
        return [user for user in self._users if user.uuid == uuid].pop()

    @property
    def users(self) -> List[User]:
        return self._users
