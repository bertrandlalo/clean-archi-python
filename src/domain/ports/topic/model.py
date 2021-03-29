from dataclasses import dataclass
from datetime import datetime
from typing import Any

from domain.ports import User


@dataclass
class Topic:
    author: User
    created_date: datetime
    topic_name: str
    uuid: Any = None

    def set_id(self, id):
        self.uuid = id

    @property
    def id(self):
        return self.uuid
