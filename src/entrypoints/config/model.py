from collections.abc import Callable
from dataclasses import dataclass

from domain.ports.topic.topic_repository import AbstractTopicRepository
from domain.ports.user.user_repository import AbstractUserRepository
from domain.use_cases.create_new_topic import CreateNewTopic
from domain.use_cases.create_new_user import CreateNewUser
from domain.use_cases.get_all_users import GetAllUsers


def wsgi_do_nothing_middleware(wsgi_app):
    def middleware(environ, start_response):
        return wsgi_app(environ, start_response)

    return middleware


@dataclass
class Config:
    user_repo: AbstractUserRepository
    topic_repo: AbstractTopicRepository
    has_middleware: bool = False
    wsgi_middleware: Callable = wsgi_do_nothing_middleware

    def get_use_cases(self):
        return [
            CreateNewUser(user_repository=self.user_repo),
            GetAllUsers(user_repository=self.user_repo),
            CreateNewTopic(topic_repository=self.topic_repo)
        ]
