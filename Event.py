from event_type import EventType
class Event:
    MIN_ARRIVAL_TIME = 1.0
    MAX_ARRIVAL_TIME = 3.0
    MIN_DEPARTURE_TIME = 1.0
    MAX_DEPARTURE_TIME = 4.0

    def __init__(self, event_type, time):
        self.event_type = event_type
        self.time = time

    def get_type(self):
        return self.event_type

    def get_time(self):
        return self.time

    @staticmethod
    def calculate_time(total_time, event_type, random_number):
        if event_type == EventType.ARRIVAL:
            return total_time + (Event.MIN_ARRIVAL_TIME + ((Event.MAX_ARRIVAL_TIME - Event.MIN_ARRIVAL_TIME) * random_number))
        else:
            return total_time + Event.MIN_DEPARTURE_TIME + ((Event.MAX_DEPARTURE_TIME - Event.MIN_DEPARTURE_TIME) * random_number)

    def __lt__(self, other):
        return self.time < other.time
