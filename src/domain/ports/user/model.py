from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class User:
    first_name: str
    last_name: str
    uuid: Any = None

    def set_id(self, id):
        self.uuid = id

    @property
    def id(self):
        return self.uuid
