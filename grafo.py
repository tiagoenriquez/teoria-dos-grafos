from aresta import Aresta
from vertice import Vertice


class Grafo:
    def __init__(self, vertices: list[Vertice], direcionado: bool):
        self.vertices = vertices
        self.direcionado = direcionado
        self.arestas: list[Aresta] = []
    
    def adicionar_aresta(self, aresta: Aresta):
        origem = self.__checar_vertice(aresta.origem)
        destino = self.__checar_vertice(aresta.destino)
        self.arestas.append(aresta)
        if not self.direcionado:
            self.arestas.append(Aresta(aresta.destino, aresta.origem, aresta.distancia))
    
    def procurar_distancia(self, origem: Vertice, destino: Vertice):
        origem = self.__checar_vertice(origem)
        destino = self.__checar_vertice(destino)
        for aresta in self.arestas:
            if aresta.origem == origem and aresta.destino == destino:
                return aresta.distancia
    
    def __checar_vertice(self, vertice_procurado: Vertice):
        for vertice in self.vertices:
            if vertice.nome == vertice_procurado.nome:
                return vertice
        raise Exception(f"Este grafo não possui o vértice {vertice_procurado.nome}")
