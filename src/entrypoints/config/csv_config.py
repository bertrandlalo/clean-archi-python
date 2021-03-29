from adapters.csv_user_repository import CsvUserRepository
from entrypoints.config.model import Config

csv_config = Config(
    user_repo=CsvUserRepository(),
    topic_repo=CsvTopicRepository(),  # Todo : CSVTopicRepository

)
