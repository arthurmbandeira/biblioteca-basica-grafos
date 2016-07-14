from collections import deque

def bfs(G, s):
    for k in G:
        k.d = -1
        k.pai = None
        k.cor = "branco"
    s = G.getVertice(s)
    s.d = 0
    s.pai = None
    s.cor = "cinza"
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in u.getAdj():
            if v.cor == "branco":
                v.d = u.d + 1
                v.pai = u
                v.cor = "cinza"
                Q.append(v)
        u.cor = "preto"
        print("Vértice " + str(u.getID()) + ", Pai " + str(u.getPai()))