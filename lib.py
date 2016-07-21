#Arthur Manuel Bandeira - RA 67226

from sys import stdin
import heapq

from Grafo import Grafo
from DFS import *
from BFS import *
from SCC import *
from bellmannFord import *

def ler(G):
    line = stdin.readline()
    spt = line.split()
    x = (spt[0])
    y = (spt[1])
    z = int(spt[2])
    if (not direcionado):
        G.addAresta(x, y, z)
        G.addAresta(y, x, z)
    else:
        G.addAresta(x, y, z)
    return G

def imprimeGrafo(G):
    for v in G:
        for w in v.getAdj():
            print(v.getID(), w.getID(), v.getPeso(w))
    print("\n")

G = Grafo()
nroVertices = int(stdin.readline())
nroArestas = int(stdin.readline())
direcionado = int(stdin.readline())
for i in range(nroArestas):
    ler(G)


imprimeGrafo(G)
# inicialDFS = 'u'
# dfs(G, inicialDFS)
# print("\n")
# topologicalSort = []
# scc(G, 'c')
# bfs(G, 'a')
# print(bellmandFord(G, 1))

# print("\n")