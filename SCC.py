''' Conjunto de Funções que retorna os componentes fortemente conectados do Grafo '''

from Grafo import *
from DFS import *
tmp = 0 # Variável global de tempo

# Função que transpõe o Grafo
def grafoTransposto(G):
    Gt = Grafo()
    for v in G:
        for w in v.getAdj():
            Gt.addAresta(w.getID(), v.getID(), v.getPeso(w))
    Gt.topologicalSort = G.topologicalSort
    Gt.topologicalSort.reverse()
    return Gt

# Função de Busca em Profundidade para encontrar os componentes conexos
def dfsScc(Gt, u):
    # Inicializa os vértices do grafo
    for k in Gt:
        k.cor = "branco"
        k.pai = None
    componente = 0
    print("Lista de componentes")
    # Para cada vértice no Grafo G transposto
    for i in Gt:
        if i.getCor() == "branco": # Se o vértice ainda não foi visitado
            print("\nComponente %d" % componente)
            print(i.getID())
            componente += 1
            dfsVisitScc(i)

# Função recursiva da Busca em Profundidade
def dfsVisitScc(u):
    global tmp
    tmp = tmp + 1
    u.cor = "cinza" # Marca o vértice como visitado
    u.d = tmp
    for v in u.getAdj():
        # Caso o vértice não tenha sido visitado ainda
        if v.cor == "branco": 
            v.pai = u
            print(v.getID())
            dfsVisitScc(v)
    u.cor = "preto" # Finaliza o vértice
    tmp = tmp + 1
    u.f = tmp

# Função que encontra os componentes fortemente conexos de um Grafo G
def scc(G, u):
    dfs(G, u) # Calcula a Busca em Profundidade de G
    print("\n")
    Gt = grafoTransposto(G) # Calcula G transposto
    dfsScc(Gt, Gt.topologicalSort[0]) # Calcula a Busca em Profundidade, considerando a ordem decrescente de tempos de término