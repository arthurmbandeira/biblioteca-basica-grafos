''' Representação de um Vértice '''

from collections import OrderedDict

class Vertice:
    """Classe que representa um Vértice"""
    def __init__(self, chave):
        self.id = chave # Identificador
        self.cor = "" # Cor utilizada para marcar o estado
        self.pai = None # Vértice predecessor
        self.adj = OrderedDict() # Vértices adjacentes
        self.d = 0 # Distância do vértice inicial no caso do BFS e tempo de descoberta no DFS
        self.f = 0 # Tempo de finalização
        self.nivel = 0 # Nível na árvore

    # Adiciona vértices adjacentes
    def addVizinho(self, vizinho, peso = 0):
        self.adj[vizinho] = peso

    # Retorna os vértices adjacentes
    def getAdj(self):
        return self.adj.keys()

    # Retorna o identificador
    def getID(self):
        return self.id

    # Retorna o atributo cor
    def getCor(self):
        return self.cor

    # Retorna o vértice predecessor
    def getPai(self):
        if (self.pai):
            return self.pai.id
        else:
            return None

    # Retorna o peso da aresta com algum vértice adjacente
    def getPeso(self, vizinho):
        if (self.adj[vizinho]):
            return self.adj[vizinho]
        else: return None

    # Retorna o tempo de término
    def getTermino(self):
        return self.f

    # Retorna o nível na árvore
    def getNivel(self):
        return self.nivel