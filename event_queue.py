# 

from event import Event
from event_type import EventType
import heapq

class EventQueue:
    def __init__(self):
        self.events = []
        self.queue_size = 0

    def add(self, event_type, random_number, total_time):
        new_time = self.calculate_position(total_time, event_type, random_number)
        event_details = f"Event: {event_type}, Random Number: {random_number}, Time: {total_time}, New Time: {new_time}"
        print(event_details)  # Print event details in one line

        if event_type == EventType.ARRIVAL:
            new_event = Event(EventType.ARRIVAL, new_time)
        else:
            new_event = Event(EventType.DEPARTURE, new_time)

        heapq.heappush(self.events, new_event)

    def remove(self):
        return heapq.heappop(self.events)

    def calculate_position(self, total_time, event_type, random_number):
        if event_type == EventType.ARRIVAL:
            return total_time + (Event.MIN_ARRIVAL_TIME_CLIENT + 
                                 ((Event.MAX_ARRIVAL_TIME_CLIENT - Event.MIN_ARRIVAL_TIME_CLIENT) * random_number))
        elif event_type == EventType.DEPARTURE:
            return total_time + (Event.MIN_EXIT_REQUEST_TIME + 
                                 ((Event.MAX_EXIT_REQUEST_TIME - Event.MIN_EXIT_REQUEST_TIME) * random_number))
        else:
            raise ValueError("Unknown event type")

    def increment_queue(self):
        self.queue_size += 1

    def decrement_queue(self):
        self.queue_size -= 1

    def is_empty(self):
        return len(self.events) == 0

    def size(self):
        return len(self.events)

    def get_queue_size(self):
        return self.queue_size

    def set_queue_size(self, queue_size):
        self.queue_size = queue_size
