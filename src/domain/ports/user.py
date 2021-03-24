from dataclasses import dataclass
from typing import Literal

UserStatus = Literal["active", "contact", "deleted", "invited"]


@dataclass
class User:
    uuid: str
    name: str
    status: UserStatus
