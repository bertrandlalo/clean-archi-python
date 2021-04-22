import os
from typing import Callable, Dict, List, Type
from domain.models import commands, events

from domain.ports.topic_repository import AbstractTopicRepository
from domain.ports.user_repository import AbstractUserRepository
from domain.ports.uuid import RealUuid
from domain.services.domain_message_bus import (
    InMemoryDomainMessageBus,
)
from domain.use_cases.create_new_topic import CreateNewTopic
from domain.use_cases.create_new_user import CreateNewUser
from domain.use_cases.get_all_users import GetAllUsers
from helpers.clock import RealClock


# def wsgi_do_nothing_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         return wsgi_app(environ, start_response)

#     return middleware


class UpdateUser:
    def execute(self, event):
        pass


class RemoveTopicFromUser:
    def execute(self, event):
        pass


class Config:
    user_repo: AbstractUserRepository
    topic_repo: AbstractTopicRepository
    bus: InMemoryDomainMessageBus
    # has_middleware: bool = False
    # wsgi_middleware: Callable = wsgi_do_nothing_middleware
    def __init__(
        self,
        topic_repository: AbstractTopicRepository,
        user_repository: AbstractUserRepository,
    ):
        self.topic_repo = topic_repository
        self.user_repo = user_repository
        self.bus = InMemoryDomainMessageBus()
        self.create_new_user = CreateNewUser(
            user_repository=self.user_repo, uuid=RealUuid(), bus=self.bus
        )

        EVENT_HANDLERS: Dict[Type[events.Event], List[Callable]] = {
            events.UserCreated: [
                lambda event: self.bus.publish_event(events.EmailSentToWelcomeUser())
            ],
            events.UserConfirmed: [UpdateUser().execute],
            events.UserDeleted: [
                UpdateUser().execute,
                RemoveTopicFromUser().execute,
            ],
        }
        COMMAND_HANDLERS: Dict[Type[commands.Command], Callable] = {
            commands.CreateNewUser: self.create_new_user.execute
        }
        self.bus._event_handlers = EVENT_HANDLERS
        self.bus._command_handlers = COMMAND_HANDLERS

    def get_use_cases(self):
        return [
            self.create_new_user,
            GetAllUsers(user_repository=self.user_repo),
            CreateNewTopic(
                uuid=RealUuid(),
                clock=RealClock(),
                user_repository=self.user_repo,
                topic_repository=self.topic_repo,
            ),
        ]


def get_api_host():
    return os.environ.get("API_HOST", "localhost")


def get_api_port():
    return os.environ.get("API_PORT", 5005)


def get_api_url():
    host = get_api_host()
    port = get_api_port()
    return f"http://{host}:{port}"