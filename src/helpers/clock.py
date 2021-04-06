import abc
import asyncio
from datetime import datetime, timedelta
from typing import NewType

DateStr = NewType("DateStr", str)
date_format = "%Y-%m-%dT%H:%M:%S.%f"


def from_datetime(date: datetime) -> DateStr:
    return DateStr(date.strftime(date_format))


def to_datetime(date: DateStr) -> datetime:
    return datetime.strptime(date, date_format)


class AbstractClock(abc.ABC):
    @abc.abstractclassmethod
    def get_now(self) -> DateStr:
        raise NotImplementedError


class CustomClock(AbstractClock):
    def __init__(self):
        self._now = DateStr("2021-01-01T12:00:00.0")

    def set_next_date(self, date: DateStr):
        self._now = date

    def get_now(self) -> DateStr:
        return self._now


class RealClock(AbstractClock):
    def get_now(self) -> DateStr:
        return from_datetime(datetime.utcnow())
