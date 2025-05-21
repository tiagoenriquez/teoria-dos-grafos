from aresta import Aresta
from floyd import floyd
from grafo import Grafo
from vertice import Vertice


a = Vertice("A")
b = Vertice("B")
c = Vertice("C")
d = Vertice("D")
vertices = [a, b, c, d]
grafo = Grafo(vertices, True)

grafo.adicionar_aresta(Aresta(a, b, 8))
grafo.adicionar_aresta(Aresta(a, d, 1))
grafo.adicionar_aresta(Aresta(b, c, 1))
grafo.adicionar_aresta(Aresta(c, a, 4))
grafo.adicionar_aresta(Aresta(d, b, 2))
grafo.adicionar_aresta(Aresta(d, c, 9))

distancias = floyd(grafo)

print(distancias)
