class Grafo:
    """docstring for Grafo"""
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def addVertice(self, chave):
        self.numVertices += 1
        novoVertice = Vertice(chave)
        self.listaVertices[chave] = novoVertice
        return novoVertice

    def getVertice(self, v):
        if v in self.listaVertices:
            return self.listaVertices[v]
        else:
            return None

    def addAresta(self, f, t, peso = 0):
        if f not in self.listaVertices:
            nv = self.addVertice(f)
        if t not in self.listaVertices:
            nv = self.addVertice(t)
        self.listaVertices[f].addVizinho(self.listaVertices[t], peso)

    def getVertices(self):
        return self.listaVertices.keys()