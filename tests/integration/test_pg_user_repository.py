from sqlalchemy.engine import create_engine
from sqlalchemy.sql import select
from tests.utils.test_pg_url import test_pg_url

from src.adapters.postgres.db import (
    initialize_db,
    user_table,
    reset_db,
)
from src.adapters.postgres.pg_user_repository import PgUserRepository
from src.domain.ports.model import User


def prepare_db():
    engine = create_engine(
        test_pg_url,
        isolation_level="REPEATABLE READ",
    )
    reset_db(engine)
    initialize_db(engine)
    return engine

patrice_user = User(first_name="patrice", last_name="bertrand", uuid="pat_uuid")
anne_user = User(first_name="anne", last_name="bertrand-lalo", uuid="anne_uuid")

def test_get_from_pg_repo():
    engine = prepare_db()
    repo = PgUserRepository(
        engine=engine,
        table=user_table,
    )

    repo.add(patrice_user)
    repo.add(anne_user)

    assert repo.users == [patrice_user, anne_user]
    assert repo.get(uuid="pat_uuid") == patrice_user

