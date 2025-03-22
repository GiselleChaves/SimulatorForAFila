from Generator import Generator

class Events:
  
  def __init__(self, type, time, client=None):
    """
    Cria um evento com o tipo, tempo e cliente (se aplicável).
    - tipo: "chegada" ou "saida"
    - tempo: momento em que o evento ocorre
    - cliente: instância do cliente (opcional para eventos de chegada e saída)
    """
    self.type = type
    self.time = time
    self.client = client
    
  def __str__(self):
        return f"Evento({self.tipo}, {self.tempo}, {self.cliente})"
