from pathlib import Path

from adapters.csv_topic_repository import CsvTopicRepository
from adapters.csv_user_repository import CsvUserRepository
from domain.ports.uuid import RealUuid
from entrypoints.config.model import Config

csv_config = Config(
    user_repo=CsvUserRepository(csv_path=Path("data") / "user_repo", uuid_generator=RealUuid()),
    topic_repo=CsvTopicRepository(csv_path=Path("data") / "topic_repo", uuid_generator=RealUuid()),
)
