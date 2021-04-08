from dataclasses import dataclass


class Command:
    pass


@dataclass
class CreateNewUser(Command):
    name: str


@dataclass
class InviteUser(Command):
    name: str


@dataclass
class DeleteUser(Command):
    name: str