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
    can_wake_up: bool = True

    @abc.abstractclassmethod
    def get_now(self) -> DateStr:
        raise NotImplementedError

    @abc.abstractclassmethod
    async def sleep(self, delay: float):
        raise NotImplementedError


class CustomClock(AbstractClock):
    def __init__(self, default_date: DateStr = None) -> None:
        self.next_date: DateStr = default_date or from_datetime(datetime.now())
        self.awaken_event: asyncio.Event

    def get_now(self) -> DateStr:
        return self.next_date

    def set_next_date(self, date: DateStr):
        self.next_date = date

    def add_seconds(self, delay: float):
        self.next_date = from_datetime(
            to_datetime(self.next_date) + timedelta(seconds=delay)
        )

    async def sleep(self, delay: float):
        await self.awaken_event.wait()
        self.can_wake_up = False

    def set_awaken_event(self, awaken_event: asyncio.Event):
        self.can_wake_up = True
        self.awaken_event = awaken_event

    async def wake_up(self):
        self.awaken_event.set()


class RealClock(AbstractClock):
    def get_now(self) -> DateStr:
        return from_datetime(datetime.now())

    async def sleep(self, delay: float):
        await asyncio.sleep(delay)
