from event import Event
from datetime import datetime

def test_event_creation():
    event = Event("Meeting", datetime(2025, 12, 1, 14, 30))
    assert event.what == "Meeting"
    assert event.when == datetime(2025, 12, 1, 14, 30)