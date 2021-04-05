from domain.ports.topic_repository import AbstractTopicRepository
from domain.ports.user_repository import AbstractUserRepository
from domain.ports.uuid import RealUuid
from domain.use_cases.create_new_topic import CreateNewTopic
from domain.use_cases.create_new_user import CreateNewUser
from domain.use_cases.get_all_users import GetAllUsers
from helpers.clock import RealClock


# def wsgi_do_nothing_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         return wsgi_app(environ, start_response)

#     return middleware


class Config:
    user_repo: AbstractUserRepository
    topic_repo: AbstractTopicRepository
    # has_middleware: bool = False
    # wsgi_middleware: Callable = wsgi_do_nothing_middleware
    def __init__(
        self,
        topic_repository: AbstractTopicRepository,
        user_repository: AbstractUserRepository,
    ):
        self.topic_repo = topic_repository
        self.user_repo = user_repository

    def get_use_cases(self):
        return [
            CreateNewUser(user_repository=self.user_repo, uuid=RealUuid()),
            GetAllUsers(user_repository=self.user_repo),
            CreateNewTopic(
                uuid=RealUuid(),
                clock=RealClock(),
                user_repository=self.user_repo,
                topic_repository=self.topic_repo,
            ),
        ]
