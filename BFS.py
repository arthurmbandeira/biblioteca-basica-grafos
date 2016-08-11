''' Função que realiza a Busca em Largura no grafo, recebe o grafo e um vértice inicial como parametro '''

from collections import deque

def bfs(G, s):
    # Inicializa os vértices
    for k in G:
        k.d = -1
        k.pai = None
        k.cor = "branco"
    s = G.getVertice(s) # Inicializa o vértice inicial
    s.d = 0
    s.pai = None
    s.cor = "cinza"
    Q = deque() # Fila
    Q.append(s)
    while Q:
        u = Q.popleft() # Desenfilera u
        for v in u.getAdj(): # Para os elementos adjacentes a u
            if v.cor == "branco": #  Caso o vértice não tenha sido visitado ainda
                v.d = u.d + 1
                v.pai = u
                v.cor = "cinza"
                Q.append(v)
        u.cor = "preto" # Finaliza vértice
        print("Vértice " + str(u.getID()) + ": Pai " + str(u.getPai()) + ", Nível " + str(u.d))