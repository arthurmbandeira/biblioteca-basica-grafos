class Vertice():
    """docstring for Vertice"""
    def __init__(self, chave):
        self.id = chave
        self.cor = ""
        self.pai = None
        self.adj = {}
        self.d = 0
        self.f = 0

    def addVizinho(self, vizinho, peso = 0):
        self.adj[vizinho] = peso

    def getAdj(self):
        return self.adj.keys()

    def getID(self):
        return self.id

    def getCor(self):
        return self.cor

    def getPai(self):
        if (self.pai):
            return self.pai.id
        else:
            return None

    def getPeso(self, vizinho):
        return self.adj[vizinho]

    def getTermino(self):
        return self.f