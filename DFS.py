''' Função que realiza a Busca em Profundidade no grafo, recebe o grafo e um vértice inicial como parâmetro '''

tempo = 0 # Variável global de tempo

def dfs(G, u):
    global topologicalSort
    topologicalSort = [] # Lista de ordenação topológica
    u = G.getVertice(u) # Vértice inicial
    nivel = 0
    # Inicializa os vértices do grafo
    for k in G:
        k.cor = "branco"
        k.pai = None
        k.nivel = 0
    # Aplica DFS no vértice inicial
    if u.getCor() == "branco":
            dfsVisit(u)
    for i in G:
        # Aplica DFS nos vértices ainda não visitados
        if i.getCor() == "branco":
            i.nivel = nivel
            dfsVisit(i)
    G.topologicalSort = topologicalSort # O classe Grafo recebe sua ordenação topológica como atributo

# Função recursiva da Busca em Profundidade
def dfsVisit(u):
    global tempo
    tempo = tempo + 1
    u.cor = "cinza" # Marca o vértice como visitado
    u.d = tempo
    for v in u.getAdj():
        # Caso o vértice não tenha sido visitado ainda
        if v.cor == "branco":
            v.pai = u
            v.nivel = u.nivel + 1
            dfsVisit(v)
    u.cor = "preto" # Finaliza o vértice
    topologicalSort.append(u) #Adiciona o vértica na lista de ordenação topológica
    tempo = tempo + 1
    u.f = tempo
    print("Vertice " + str(u.getID()) + ": Pai " + str(u.getPai()) + ", Nivel " + str(u.getNivel()))