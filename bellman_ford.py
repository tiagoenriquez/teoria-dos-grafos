from grafo import Grafo
from vertice import Vertice


def bellman_ford(grafo: Grafo, origem: Vertice):
    distancias = {vertice.nome: float("inf") for vertice in grafo.vertices}
    predecessores = {vertice.nome: None for vertice in grafo.vertices}
    distancias[origem.nome] = 0

    for _ in range(len(grafo.vertices) - 1):
        for aresta in grafo.arestas:
            if distancias[aresta.origem.nome] + aresta.distancia < distancias[aresta.destino.nome]:
                distancias[aresta.destino.nome] = distancias[aresta.origem.nome] + aresta.distancia
                predecessores[aresta.destino.nome] = aresta.origem.nome
    
    for aresta in grafo.arestas:
        if distancias[aresta.origem.nome] + aresta.distancia < distancias[aresta.destino.nome]:
            raise Exception("O grafo contém um ciclo de peso negativo.")

    return distancias
