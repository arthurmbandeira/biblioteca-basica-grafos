#Arthur Manuel Bandeira - RA 67226

from sys import stdin
import argparse

from Grafo import Grafo
from DFS import *
from BFS import *
# from SCC import *

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

def grafoTransposto(G):
    Gt = Grafo()
    for v in G:
        for w in v.getAdj():
            Gt.addAresta(w.getID(), v.getID(), v.getPeso(w))
    return Gt

def dfsScc(Gt, u):
    for k in Gt:
        k.cor = "branco"
        k.pai = None
    componente = 1
    print("Lista de componentes")
    for i in Gt:
        if i.getCor() == "branco":
            print("\nComponente %d" % componente)
            print(i.getID())
            dfsVisitScc(i)
            componente += 1

def dfsVisitScc(u):
    global tempo
    tempo = tempo + 1
    u.cor = "cinza"
    u.d = tempo
    for v in u.getAdj():
        if v.cor == "branco":
            v.pai = u
            print(v.getID())
            dfsVisitScc(v)
    u.cor = "preto"
    tempo = tempo + 1
    u.f = tempo

def scc(G, u):
    dfs(G, u)
    print("\n")
    Gt = grafoTransposto(G)
    Gt.topologicalSort = G.topologicalSort
    Gt.topologicalSort.reverse()
    dfsScc(Gt, Gt.topologicalSort[0])

G = Grafo()
nroVertices = int(stdin.readline())
nroArestas = int(stdin.readline())
direcionado = int(stdin.readline())
for i in range(nroArestas):
    ler(G)
# for v in G:
#     for w in v.getAdj():
#         print("(%d, %d, %d)" % (v.getID(), w.getID(), v.getPeso(w)))

# inicialDFS = int(input("Vértice Inicial DFS: "))
# parser = argparse.ArgumentParser(description="Entrada de dados.")

# inicialDFS = 1
# dfs(G, inicialDFS)
print("\n")
tempo = 0
# topologicalSort = []
scc(G, 3)
# bfs(G, 2)

print("\n")