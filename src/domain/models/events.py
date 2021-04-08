from dataclasses import dataclass


class Event:
    pass


@dataclass
class UserConfirmed(Event):
    uuid: str


@dataclass
class EmailSentToWelcomeUser(Event):
    pass


@dataclass
class UserDeleted(Event):
    uuid: str


@dataclass
class UserCreated(Event):
    name: str