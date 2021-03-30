from dataclasses import dataclass
from typing import Literal

from src.domain.ports.user import User

TopicStatus = Literal["active", "archived"]


@dataclass
class Topic:
    uuid: str
    topic_text: str
    topic_short: str
    title: str
    description: str
    status: TopicStatus
    # author: User