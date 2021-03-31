import uuid as uuid_lib
from abc import ABC, abstractmethod
from typing import List


def uuid4() -> str:
    return str(uuid_lib.uuid4())


class AbstractUuid(ABC):
    @abstractmethod
    def make(self) -> str:
        raise NotImplementedError


class CustomUuid(AbstractUuid):
    def __init__(self, uuid: str = None) -> None:
        self._next_uuids = []
        if uuid:
            self._next_uuids = [uuid]

    def make(self) -> str:
        return (
            self._next_uuids.pop(0)
            if self._next_uuids
            else f"generated_from_custom_uuid_{uuid4()}"
        )

    def set_next_uuid(self, uuid: str):
        self._next_uuids = [uuid]

    def set_next_uuids(self, uuids: List[str]):
        self._next_uuids = uuids


class RealUuid(AbstractUuid):
    def make(self) -> str:
        return uuid4()
