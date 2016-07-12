#Arthur Manuel Bandeira - RA 67226

from sys import stdin
import argparse
from Grafo import Grafo

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

def dfs(G, u):
    for u in G:
        u.cor = "branco"
        u.pai = None
    tempo = 0
    for u in G:
        if u.cor == "branco":
            dfsVisit(u, tempo)

# Sempre começando em 0, alterar
def dfsVisit(u, tempo):
    tempo += 1
    u.cor = "cinza"
    u.d = tempo
    for v in u.getAdj():
        if v.cor == "branco":
            v.pai = u
            dfsVisit(v, tempo)
    u.cor = "preto"
    tempo += 1
    u.f = tempo
    print("Vértice " + str(u.getID()) + ", Pai " + str(u.getPai()))

G = Grafo()
nroVertices = int(stdin.readline())
nroArestas = int(stdin.readline())
direcionado = int(stdin.readline())
for i in range(nroArestas):
    ler(G)
for v in G:
    for w in v.getAdj():
        print("(%d, %d, %d)" % (v.getID(), w.getID(), v.getPeso(w)))

# inicialDFS = int(input("Vértice Inicial DFS: "))
# parser = argparse.ArgumentParser(description="Entrada de dados.")
inicialDFS = 5
dfs(G, inicialDFS)