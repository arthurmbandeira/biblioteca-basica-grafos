#Arthur Manuel Bandeira - RA 67226

import argparse
import heapq

import tkinter as tk

from Grafo import Grafo
from DFS import *
from BFS import *
from SCC import *
from bellmannFord import *

def ler(G):
    line = f.readline()
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

f = open('testes/teste2.txt', 'r')

nroVertices = int(f.readline())
nroArestas = int(f.readline())
direcionado = int(f.readline())
for i in range(nroArestas):
    ler(G)


inicialDFS = input("Vértice Inicial DFS: ")

print(inicialDFS)
# parser = argparse.ArgumentParser(description="Entrada de dados.")

imprimeGrafo(G)
# inicialDFS = 'u'
# dfs(G, inicialDFS)
# print("\n")
# topologicalSort = []
scc(G, inicialDFS)
# bfs(G, 'a')
# print(bellmandFord(G, '1'))
# caminhoBF(G, 's', 'x')

print("\n")

# root = tk.Tk()

# root.title("Grafos")
# root.geometry("800x600")

# root.mainloop()