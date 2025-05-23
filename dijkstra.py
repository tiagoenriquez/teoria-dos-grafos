import heapq

from grafo import Grafo
from vertice import Vertice


def dijkstra(grafo: Grafo, origem: Vertice):
    distancias = {vertice.nome: float('inf') for vertice in grafo.vertices}
    predecessores = {vertice.nome: None for vertice in grafo.vertices}
    distancias[origem.nome] = 0
    
    fila_de_prioridade = [(0, origem)]
    
    while fila_de_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_de_prioridade)
        print(f"Vértice atual: {vertice_atual.nome}")

        for aresta in grafo.procurar_arestas_de_origem(vertice_atual):
            vizinho = aresta.destino
            nova_distancia = distancia_atual + aresta.distancia

            if nova_distancia < distancias[vizinho.nome]:
                distancias[vizinho.nome] = nova_distancia
                predecessores[vizinho.nome] = vertice_atual.nome
                heapq.heappush(fila_de_prioridade, (nova_distancia, vizinho))
        
        print(f"Distâncias atuais: {distancias}\n")
    
    return distancias
