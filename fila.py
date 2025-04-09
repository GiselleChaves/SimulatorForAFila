from event import Event
from event_type import EventType
from event_queue import EventQueue
from collections import deque

class Fila:

    id = 0

    queue = EventQueue()
    
    arrival_time = 1.0
    
    lambda_value = 2  # Quantidade de servidores
    queue_state = 3  # Tamanho máximo da fila

    estado_fila = [0] * (queue_state + 1)

    min_arrival_time = 1.0
    max_arrival_time = 3.0
    min_exit_request_time = 3.0
    max_exit_request_time = 4.0
    random_numbers = deque([0.7, 0.1, 0.1, 0.9, 0.2, 0.7])
    
    total_time = 0.0

    def __init__(self, id, queue_state, lambda_value, arrival_time, random_number, min_arrival_time, max_arrival_time, min_exit_request_time, max_exit_request_time):
        self.id = id
        self.queue_state = queue_state
        self.lambda_value = lambda_value
        self.min_arrival_time = min_arrival_time
        self.max_arrival_time = max_arrival_time
        self.min_exit_request_time = min_exit_request_time
        self.max_exit_request_time = max_exit_request_time
        self.estado_fila = [0] * (queue_state + 1)
        self.arrival_time = arrival_time
        self.queue = EventQueue()
        self.total_time = 0.0
        self.random_numbers = random_number
    
    def exec(self):
        if self.total_time == 0.0:
            current_event = Event(EventType.ARRIVAL, self.arrival_time)
        else:
            current_event = self.queue.remove()
        
        last_event_time = self.total_time
        self.total_time = current_event.time

        if current_event.event_type == EventType.ARRIVAL:
            if self.queue.size() < self.queue_state:
                self.estado_fila[self.queue.get_queue_size()] += self.total_time - last_event_time
                self.queue.increment_queue()
                if self.queue.get_queue_size() <= self.lambda_value:
                    self.queue.add(EventType.DEPARTURE, self.random_numbers.next_random_number(), self.total_time, self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)

            self.queue.add(EventType.ARRIVAL, self.random_numbers.next_random_number(), self.total_time, self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)
            print(f"Queue {self.id} - size: {self.estado_fila}")
            print(f"Queue {self.id} - total time: {self.total_time}")
        else:
            self.estado_fila[self.queue.get_queue_size()] += self.total_time - last_event_time
            self.queue.decrement_queue()
            if self.queue.get_queue_size() >= self.lambda_value:
                self.queue.add(EventType.DEPARTURE, self.random_numbers.next_random_number(), self.total_time, self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)
            print(f"Queue {self.id} - size: {self.estado_fila}")
            print(f"Queue {self.id} - total time: {self.total_time}")
            return Event(EventType.DEPARTURE, self.total_time)
    
    def exec_with_event(self, event):
        
        self.queue.add(EventType.ARRIVAL, self.random_numbers.next_random_number(), event.get_time(), self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)
        
        current_event = self.queue.remove()
        
        last_event_time = self.total_time
        self.total_time = current_event.time

        if current_event.event_type == EventType.ARRIVAL:
            if self.queue.size() < self.queue_state:
                self.estado_fila[self.queue.get_queue_size()] += self.total_time - last_event_time
                self.queue.increment_queue()
                if self.queue.get_queue_size() <= self.lambda_value:
                    self.queue.add(EventType.DEPARTURE, self.random_numbers.next_random_number(), self.total_time, self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)

            self.queue.add(EventType.ARRIVAL, self.random_numbers.next_random_number(), self.total_time, self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)
            print(f"Queue {self.id} - size: {self.estado_fila}")
            print(f"Queue {self.id} - total time: {self.total_time}")
        else:
            self.estado_fila[self.queue.get_queue_size()] += self.total_time - last_event_time
            self.queue.decrement_queue()
            if self.queue.get_queue_size() >= self.lambda_value:
                self.queue.add(EventType.DEPARTURE, self.random_numbers.next_random_number(), self.total_time, self.min_arrival_time, self.max_arrival_time, self.min_exit_request_time, self.max_exit_request_time)
            print(f"Queue {self.id} - size: {self.estado_fila}")
            print(f"Queue {self.id} - total time: {self.total_time}")
            return Event(EventType.DEPARTURE, self.total_time)
        
    