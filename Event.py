from event_type import EventType
class Event:

    def __init__(self, event_type, time):
        self.event_type = event_type
        self.time = time

    def get_type(self):
        return self.event_type

    def get_time(self):
        return self.time

    def __lt__(self, other):
        return self.time < other.time
