from sqlalchemy import Column, MetaData, String, Table

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("name", String(255)),
    Column("status", String(255)),
    Column("uuid", String(255)),
)


def initialize_db(engine):
    metadata.create_all(engine)


def reset_db(engine):
    metadata.drop_all(engine)
