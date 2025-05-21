from grafo import Grafo


def floyd(grafo: Grafo):
    vertices = grafo.vertices
    distancias = [[float('inf')] * len(vertices) for _ in range(len(vertices))]

    for i, vertice_i in enumerate(vertices):
        for j, vertice_j in enumerate(vertices):
            if i == j:
                distancias[i][j] = 0
            else:
                distancia = grafo.procurar_distancia(vertice_i, vertice_j)
                if distancia and distancia > 0:
                    distancias[i][j] = distancia
    
    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
    
    return distancias
