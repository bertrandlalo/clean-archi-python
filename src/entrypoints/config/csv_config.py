from pathlib import Path

from adapters.csv_topic_repository import CsvTopicRepository
from adapters.csv_user_repository import CsvUserRepository
from entrypoints.config.config import Config

csv_config = Config(
    user_repository=CsvUserRepository(csv_path=Path("data") / "user_repo"),
    topic_repository=CsvTopicRepository(csv_path=Path("data") / "topic_repo"),
)
