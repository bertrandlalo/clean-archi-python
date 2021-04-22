from dataclasses import dataclass
from domain.models.events import Event
from domain.models.user import User
from domain.ports.user_repository import AbstractUserRepository
from domain.ports.uuid import AbstractUuid
from domain.services.domain_message_bus import AbstractDomainMessageBus

from domain.models import commands, events

# class UserNameAlreadyExists(Exception):
#     pass
@dataclass
class UserNameAlreadyExists(Event):
    name: str
    status: str


class CreateNewUser:
    def __init__(
        self,
        user_repository: AbstractUserRepository,
        uuid: AbstractUuid,
        bus: AbstractDomainMessageBus,
    ) -> None:
        self.user_repository = user_repository
        self.uuid = uuid
        self.bus = bus

    # def execute(self, name: str):
    def execute(self, command: commands.CreateNewUser):
        name = command.name

        user_by_name = self.user_repository.get_by_name(name)
        if user_by_name:
            result_event = UserNameAlreadyExists(name, user_by_name.status)
            # raise UserNameAlreadyExists()
        else:
            uuid = self.uuid.make()
            user = User(name=name, status="pending", uuid=uuid)
            self.user_repository.add(user)
            result_event = events.UserCreated(name=name)

        self.bus.publish_event(result_event)
        return result_event
