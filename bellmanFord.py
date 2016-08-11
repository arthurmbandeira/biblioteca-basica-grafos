''' Conjunto de funções que encontram o caminho mínimo utilizando o algoritmo de Bellman Ford '''

# Função para inicializar os vértices
def initializeSingleSource(G, s):
    for i in G:
        i.d = float('Inf')
        i.pai = None
    s.d = 0

# Função que faz o relaxamento das arestas
def relax(u, v):
    if v.d > u.d + u.getPeso(v): # Testa se o caminho entre u e v pode ser melhorado
        v.d = u.d + u.getPeso(v)
        v.pai = u

# Método de caminho mínimo Bellman Ford
def bellmanFord(G, s):
    s = G.getVertice(s)
    initializeSingleSource(G, s)
    # Sendo V o numero de vértices no grafo, faz o relaxamento das arestas V - 1 vezes
    for i in range(G.numVertices - 1): 
        for u in G:
            for v in u.getAdj():
                relax(u, v)
    # Caso o grafo ainda apresente arestas que possam ser relaxadas, o Grafo tem ciclo negativo, então o algoritmo retorna Falso
    for u in G:
            for v in u.getAdj():
                if v.d > (u.d + u.getPeso(v)):
                    return False
    # Caso não haja ciclos negativos, retorna Verdadeiro
    return True

# Função para imprimir o resultado do Bellman Ford
def caminhoBF(G, s, t):
    s = G.getVertice(s)
    t = G.getVertice(t)
    if t not in G: # Caso o vértice escolhido como destino não pertença ao Grafo
        print("Vertice destino nao pertence ao Grafo")
        return
    atual = t
    pesoTotal = 0
    if bellmanFord(G, s.getID()): # Se o Grafo não tem ciclo negativo, imprime o caminho
        print("Caminho composto por: ")
        while(atual != s):
            pesoTotal = pesoTotal + atual.pai.getPeso(atual)
            if atual:
                print("Vértice " + str(atual.getID()))
            atual = atual.pai
        print("Vértice " + s.getID())
        print("Peso total do caminho: " + str(pesoTotal))
    else: # Se o Grafo tem ciclo negativo
        print("O grafo apresenta um ciclo negativo.")