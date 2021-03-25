from dataclasses import asdict
from typing import List

from sqlalchemy import Table
from sqlalchemy.engine.base import Engine

from domain.ports.user import User
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

    def get_all(self) -> List[User]:
        raise NotImplementedError
