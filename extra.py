
def tarjan(G):
    index = 0
    S = []
    for v in G:
        if G.getVertice(v).cor == "branco":
            strongConnect(v, index, S)

def strongConnect(v, index, S):
    v.lowLink = index
    index += 1
    S.append(v)
    v.naPilha = True
    for w in v.getAdj():
        if w.cor == "branco":
            strongConnect(w)
            v.lowLink = min(v.getLowLink(), w.getLowLink())
        elif w.getNaPilha():
            v.lowLink = min(v.getLowLink(), w.getID())
    if (v.getLowLink() == v.getID()):
        SCC = []