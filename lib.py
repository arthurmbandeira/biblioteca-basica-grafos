#Arthur Manuel Bandeira - RA 67226

from sys import stdin

def ler(G):
    line = stdin.readline()
    spt = line.split()
    x = int(spt[0])
    y = int(spt[1])
    z = int(spt[2])
    if (not direcionado):
        print("To Do")
    else:
        if x in G.keys():
            G[x].append((y, z))
        else:
            G[x] = [(y, z)]
    return G


G = dict()
nroVertices = int(stdin.readline())
nroArestas = int(stdin.readline())
direcionado = int(stdin.readline())
for i in range(nroArestas):
    ler(G)
print(G)