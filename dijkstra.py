def initializeSingleSource(G, s):
    for i in G:
        i.d = -1
        v.pai = None
    s.d = 0

def relax(u, v):
    if v.d > u.d + u.getPeso(v):
        v.d = u.d + u.getPeso(v)
        v.pai = u