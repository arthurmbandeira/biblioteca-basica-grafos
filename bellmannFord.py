def initializeSingleSource(G, s):
    for i in G:
        i.d = float('Inf')
        i.pai = None
    s.d = 0

def relax(u, v):
    if v.d > u.d + u.getPeso(v):
        v.d = u.d + u.getPeso(v)
        v.pai = u

def bellmandFord(G, s):
    s = G.getVertice(s)
    initializeSingleSource(G, s)
    for i in range(G.numVertices - 1):
        for u in G:
            for v in u.getAdj():
                relax(u, v)
    for u in G:
            for v in u.getAdj():
                if v.d > (u.d + u.getPeso(v)):
                    return False
    return True