from dataclasses import dataclass
from datetime import datetime
from typing import Any

from helpers.clock import DateStr

# from google.cloud import ndb


# class String:
#     normal = str
#     ndb_repr = ndb.StringProperty


@dataclass
class Topic:
    author_uuid: str
    topic_name: str
    created_date: DateStr  # datetime
    uuid: str

    # def set_id(self, id):
    #     self.uuid = id

    # @property
    # def id(self):
    #     return self.uuid
