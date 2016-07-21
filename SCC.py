from Grafo import *
from DFS import *
tempo = 0

def grafoTransposto(G):
    Gt = Grafo()
    for v in G:
        for w in v.getAdj():
            Gt.addAresta(w.getID(), v.getID(), v.getPeso(w))
    Gt.topologicalSort = G.topologicalSort
    Gt.topologicalSort.reverse()
    return Gt

def dfsScc(Gt, u):
    for k in Gt:
        k.cor = "branco"
        k.pai = None
    componente = 0
    print("Lista de componentes")
    for i in Gt:
        if i.getCor() == "branco":
            print("\nComponente %d" % componente)
            print(i.getID())
            componente += 1
            dfsVisitScc(i)

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
    dfsScc(Gt, Gt.topologicalSort[0])