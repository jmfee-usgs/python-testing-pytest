from unittest import mock

from examples.event_list import EventList
from examples.event_service import EventService


@mock.patch.object(EventList, "format_event")
def test_event_list(format_event):
    """Entire methods can be replaced to isolate"""
    # arrange
    features = [
        {"properties": {"mag": "1.2", "place": "place1"}},
        {"properties": {"mag": "2.3", "place": "place2"}},
    ]
    service = EventService()
    service.get_events = mock.Mock(return_value=features)
    eventlist = EventList(service)
    # act
    formatted = eventlist.get_list()
    # assert
    format_event.assert_called_
    assert formatted == "M1.2 - place1\nM2.3 - place2"
