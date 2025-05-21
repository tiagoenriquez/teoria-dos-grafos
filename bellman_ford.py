from aresta import Aresta
import aresta
from grafo import Grafo
from vertice import Vertice


def bellmanFord(grafo: Grafo, origem: Vertice):
    destinos = grafo.vertices
    for destino in destinos:
        distancia = grafo.procurar_distancia(origem, destino)
        if not distancia:
            if origem.nome == destino.nome:
                distancia = 0
            else:
                distancia = float('inf')
            aresta = Aresta(origem, destino, distancia)
            grafo.adicionar_aresta(aresta)
    
    ## incompleto
