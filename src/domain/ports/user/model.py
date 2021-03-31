from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

UserStatus = Literal["active", "contact", "deleted", "invited"]


@dataclass
class User:
    name: str
    status: UserStatus
    uuid: Any = None

    def set_id(self, id):
        self.uuid = id

    @property
    def id(self):
        return self.uuid
