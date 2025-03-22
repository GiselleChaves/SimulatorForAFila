class Simulator:

  def __init__(self, gerador, fila_capacity=5):
        self.gerador = gerador
        self.clients = []
        self.service_time = 0
        self.fila_capacity = fila_capacity
        self.events = []
  
  
