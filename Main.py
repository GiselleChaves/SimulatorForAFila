from collections import deque
from event import Event
from event_type import EventType
from event_queue import EventQueue
from Generator import Generator
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
    random_numbers = Generator(89,226,564371982,14)
    
    total_time = 0.0

    fila = Fila(1, 2, 3, 1.5, random_numbers, min_arrival_time, max_arrival_time, min_exit_request_time, max_exit_request_time)
    fila2 = Fila(2, 1, 5, 0, random_numbers, 0.0, 0.0, 2.0, 3.0)
    for i in range(100):
        event = fila.exec()
        if event:
            fila2.exec_with_event(event)
    

if __name__ == "__main__":
    main()
