from dataclasses import asdict
from typing import List

from sqlalchemy import Table
from sqlalchemy.engine.base import Engine

from domain.models.user import User
from domain.ports.user_repository import AbstractUserRepository


class PgUserRepository(AbstractUserRepository):
    def __init__(
        self,
        engine: Engine,
        table: Table,
    ) -> None:
        self.connection = engine.connect()
        self.table = table

    def add(self, user: User) -> None:
        insertion = self.table.insert().values(**asdict(user))
        self.connection.execute(insertion)

    def get(self, uuid: str) -> User:
        s = self.table.select().where(self.table.c.uuid == uuid)
        rows = self.connection.execute(s)
        return User(*list(rows)[0])

    def get_all(self) -> List[User]:
        raise NotImplementedError

    def get_by_name(self) -> User:
        raise NotImplementedError

    @property
    def users(self) -> List[User]:
        s = self.table.select()
        rows = self.connection.execute(s)
        return [User(*row) for row in rows]
