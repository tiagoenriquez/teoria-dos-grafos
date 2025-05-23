class Vertice:
    def __init__(self, nome: str):
        self.nome = nome
        self.distancia = float('inf')
    
    def __lt__(self, outro: "Vertice"):
        return self.distancia < outro.distancia
