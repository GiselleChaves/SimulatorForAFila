from collections import deque
from event import Event
from event_type import EventType
from event_queue import EventQueue
from fila import Fila

def main():
    
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
    initial_event = Event(EventType.ARRIVAL, arrival_time)

    fila = Fila(lambda_value, queue_state, arrival_time, random_numbers, min_arrival_time, max_arrival_time, min_exit_request_time, max_exit_request_time)
    fila2 = Fila(lambda_value, queue_state, arrival_time, random_numbers, min_arrival_time, max_arrival_time, min_exit_request_time, max_exit_request_time)
    while random_numbers:
        event = fila.exec(initial_event)
        if event is not None:
            fila2.exec(event)

if __name__ == "__main__":
    main()
