from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

UserStatus = Literal["active", "contact", "deleted", "invited"]


@dataclass
class User:
    name: str
    status: UserStatus
    uuid: str

    # def set_id(self, id):
    #     self.uuid = id
    # @property
    # def id(self):
    #     return self.uuid
