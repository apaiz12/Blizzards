#Create an Event class that has attributes: what (str) and when (DateTime). 
# Create a constructor and __str__ methods.
from datetime import datetime
class Event:
    def __init__(self, what: str, when: datetime):
        self.what = what
        self.when = when

    def __str__(self):
        formatted_time = self.when.strftime("%m/%d/%Y at %I:%M %p")
        return f"Event: {self.what} at {formatted_time}"
    # Use Case 1: Remove all events matching this event's "what"
    def remove_event(self, event_list: list):
        original_len = len(event_list)
        event_list[:] = [e for e in event_list if e.what != self.what]
        return len(event_list) < original_len