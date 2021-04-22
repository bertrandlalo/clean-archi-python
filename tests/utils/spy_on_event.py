from typing import Any, Type, List

from domain.services.domain_message_bus import (
    AbstractDomainMessageBus,
)
from domain.models import events


def spy_on_event(
    event_bus: AbstractDomainMessageBus, event_type: Type[events.Event]
) -> List[Any]:
    published_events = []

    def spy(e):
        published_events.append(e)

    event_bus.subscribe_to_event(event_type, spy)
    return published_events