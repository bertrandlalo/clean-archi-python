from sqlalchemy import Column, MetaData, String, Table
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("uuid", String(255)),
)


def initialize_db(engine):
    metadata.create_all(engine)


def reset_db(engine):
    metadata.drop_all(engine)
