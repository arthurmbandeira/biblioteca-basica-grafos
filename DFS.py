tmp = 0

def dfs(G, u):
    global topologicalSort
    topologicalSort = []
    u = G.getVertice(u)
    for k in G:
        k.cor = "branco"
        k.pai = None
    for i in G:
        if u.getCor() == "branco":
            dfsVisit(u)
        if i.getCor() == "branco":
            dfsVisit(i)

def dfsVisit(u):
    global tmp
    tmp = tmp + 1
    u.cor = "cinza"
    u.d = tmp
    for v in u.getAdj():
        if v.cor == "branco":
            v.pai = u
            dfsVisit(v)
    u.cor = "preto"
    topologicalSort.append(u.getID())
    tmp = tmp + 1
    u.f = tmp
    print("Vértice " + str(u.getID()) + ", Pai " + str(u.getPai()) + ", Início " + str(u.d) + ", Término " + str(u.f))