from collections import deque
from event import Event
from event_type import EventType
from event_queue import EventQueue

def main():
    
    queue = EventQueue()
    
    arrival_time = 1.0
    
    lambda_value = 2  
    queue_state = 2 

    Event.MIN_ARRIVAL_TIME_CLIENT = 1.0
    Event.MAX_ARRIVAL_TIME_CLIENT = 3.0

    Event.MIN_EXIT_REQUEST_TIME = 3.0
    Event.MAX_EXIT_REQUEST_TIME = 4.0
    random_numbers = deque([0.7, 0.1, 0.1, 0.9, 0.2, 0.7])
    
    total_time = 0.0

    while random_numbers:
        if total_time == 0.0:
            current_event = Event(EventType.ARRIVAL, arrival_time)
        else:
            current_event = queue.remove()

        total_time = current_event.time

        if current_event.event_type == EventType.ARRIVAL:
            if queue.size() < queue_state:
                queue.increment_queue()
                if queue.get_queue_size() <= lambda_value:
                    queue.add(EventType.DEPARTURE, random_numbers.popleft(), total_time)

            queue.add(EventType.ARRIVAL, random_numbers.popleft(), total_time)
        else:
            queue.decrement_queue()
            if queue.get_queue_size() >= lambda_value:
                queue.add(EventType.DEPARTURE, random_numbers.popleft(), total_time)

    print(f"Total time: {total_time}")

if __name__ == "__main__":
    main()
