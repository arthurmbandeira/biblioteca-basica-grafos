#Arthur Manuel Bandeira - RA 67226

from sys import stdin
import argparse
import heapq

from Grafo import Grafo
from DFS import *
from BFS import *
from SCC import *
from bellmannFord import *

def ler(G):
    line = stdin.readline()
    spt = line.split()
    x = int(spt[0])
    y = int(spt[1])
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
            print("(%d, %d, %d)" % (v.getID(), w.getID(), v.getPeso(w)))
    print("\n")

G = Grafo()
nroVertices = int(stdin.readline())
nroArestas = int(stdin.readline())
direcionado = int(stdin.readline())
for i in range(nroArestas):
    ler(G)

# inicialDFS = int(input("Vértice Inicial DFS: "))
# parser = argparse.ArgumentParser(description="Entrada de dados.")

imprimeGrafo(G)
inicialDFS = 1
dfs(G, inicialDFS)
print("\n")
# topologicalSort = []
# scc(G, 4)
# bfs(G, 2)
# print(bellmandFord(G, 1))

print("\n")