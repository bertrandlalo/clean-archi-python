import csv
import os
from pathlib import Path
from typing import List, Optional, Type

from domain.ports import User
from domain.ports.user.user_repository import (
    AbstractUserRepository,
)
from domain.ports.uuid import AbstractUuid


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
        csv_columns = [
            "uuid",
            "name",
            "status",
        ]  # equivalent to User.__annotations__.keys()
        if os.path.isfile(self.csv_path):
            self._users = self._from_csv()
        else:
            mkdir_if_relevant(self.csv_path.parent)
            writerow(self.csv_path, csv_columns)

    def add(self, user: User):
        self._users.append(user)
        id = self.uuid_generator.make()

        writerow(
            self.csv_path,
            [
                id,
                user.name,
                user.status,
            ],
        )
        user.set_id(id)

    def _from_csv(self) -> List[User]:
        loaded_users = []
        with self.csv_path.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                loaded_users.append(User(**row))
        return loaded_users

    def get(self, uuid: str) -> Optional[User]:
        return [user for user in self._users if user.uuid == uuid].pop()

    def get_all(self) -> List[User]:
        return self._users

    @property
    def users(self) -> List[User]:
        return self._users
