import abc
from collections import defaultdict
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Type,
)

from domain.models import commands, events


class AbstractDomainMessageBus(abc.ABC):
    _event_handlers: Dict[Type[events.Event], List[Callable]]
    _command_handlers: Dict[Type[commands.Command], Callable]

    @abc.abstractclassmethod
    def subscribe_to_event(
        self, event_type: Type[events.Event], callback: Callable
    ) -> None:
        raise NotImplementedError()

    @abc.abstractclassmethod
    def publish_event(self, event: events.Event) -> None:
        raise NotImplementedError()

    @abc.abstractclassmethod
    async def publish_command(self, command: commands.Command) -> None:
        raise NotImplementedError()


class InMemoryDomainMessageBus(AbstractDomainMessageBus):
    def __init__(
        self,
        event_handlers: Optional[Dict[Type[events.Event], List[Callable]]] = None,
        command_handlers: Optional[Dict[Type[commands.Command], Callable]] = None,
    ) -> None:
        self._event_handlers = event_handlers or defaultdict(lambda: [])
        self._command_handlers = command_handlers or {}

    def subscribe_to_event(
        self, event_type: Type[events.Event], callback: Callable
    ) -> None:
        if event_type in self._event_handlers:
            self._event_handlers[event_type].append(callback)
        else:
            self._event_handlers[event_type] = [callback]

    def publish_event(self, event: events.Event) -> None:
        handlers = self._event_handlers.get(type(event))
        if handlers:
            print("Handle event ", type(event))
            for callback in handlers:
                callback(event)

    def publish_command(self, command: commands.Command) -> None:
        handler = self._command_handlers.get(type(command))
        if handler:
            print("Handle command ", type(command))
            return handler(command)
