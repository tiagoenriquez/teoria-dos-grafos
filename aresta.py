from vertice import Vertice


class Aresta:
    def __init__(self, origem: Vertice, destino: Vertice, distancia: float):
        self.origem = origem
        self.destino = destino
        self.distancia = distancia
