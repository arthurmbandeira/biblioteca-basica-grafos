tmp = 0

def dfs(G, u):
    global topologicalSort
    topologicalSort = []
    u = G.getVertice(u)
    nivel = 0
    for k in G:
        k.cor = "branco"
        k.pai = None
        k.nivel = 0
    if u.getCor() == "branco":
            dfsVisit(u)
    for i in G:
        if i.getCor() == "branco":
            i.nivel = nivel
            dfsVisit(i)
    G.topologicalSort = topologicalSort

def dfsVisit(u):
    global tmp
    tmp = tmp + 1
    u.cor = "cinza"
    u.d = tmp
    for v in u.getAdj():
        if v.cor == "branco":
            v.pai = u
            v.nivel = u.nivel + 1
            dfsVisit(v)
    u.cor = "preto"
    topologicalSort.append(u)
    tmp = tmp + 1
    u.f = tmp
    print("Vértice " + str(u.getID()) + ": Pai " + str(u.getPai()) + ", Nível " + str(u.getNivel()))