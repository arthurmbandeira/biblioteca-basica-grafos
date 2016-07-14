def grafoTransposto(G):
    Gt = Grafo()
    for v in G:
        for w in v.getAdj():
            Gt.addAresta(w.getID(), v.getID(), v.getPeso(w))
    return Gt

def dfsScc(Gt, listaDecrescente):
    for k in listaDecrescente:
        Gt.getVertice(k).cor = "branco"
        Gt.getVertice(k).pai = None
    for i in listaDecrescente:
        if Gt.getVertice(i).cor == "branco":
            dfsVisitScc(Gt.getVertice(i))

def dfsVisitScc(u):
    global tempo
    tempo = tempo + 1
    u.cor = "cinza"
    u.d = tempo
    for v in u.getAdj():
        if v.cor == "branco":
            v.pai = u
            dfsVisit(v)
    u.cor = "preto"
    tempo = tempo + 1
    u.f = tempo
    print("Vértice " + str(u.getID()) + ", Pai " + str(u.getPai()) + ", Início " + str(u.d) + ", Término " + str(u.f))

def scc(G, u):
    dfs(G, u)
    Gt = grafoTransposto(G)
    l = []
    for v in G:
        l.append(v.f)
    l.sort(reverse=True)
    dfs(Gt, Gt.getVertice())