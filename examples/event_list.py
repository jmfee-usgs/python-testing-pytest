from typing import Dict, Optional

from .event_service import EventService


class EventList:
    def __init__(self, service: Optional[EventService] = None):
        self.service = service or EventService()

    def format_event(self, feature: Dict) -> str:
        props = feature["properties"]
        mag = props["mag"]
        place = props["place"]
        return f"M{mag} - {place}"

    def get_list(self) -> str:
        events = self.service.get_events()
        list = "\n".join([self.format_event(e) for e in events])
        return list

    def untested_function(self):
        if float("1") != 1:
            raise ValueError("this never happens")
