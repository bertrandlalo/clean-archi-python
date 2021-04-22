from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

UserStatus = Literal["pending", "active", "contact", "deleted", "invited"]


@dataclass
class User:
    name: str
    status: UserStatus
    uuid: str
