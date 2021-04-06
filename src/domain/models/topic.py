from dataclasses import dataclass

from helpers.clock import DateStr


@dataclass
class Topic:
    author_uuid: str
    topic_name: str
    uuid: str
    created_date: DateStr
