from Vertice import Vertice
from collections import OrderedDict

class Grafo:
    """docstring for Grafo"""
    def __init__(self):
        self.listaVertices = OrderedDict()
        self.numVertices = 0
        self.topologicalSort = []

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

    def addAresta(self, atual, vizinho, peso = 0):
        if atual not in self.listaVertices:
            nv = self.addVertice(atual)
        if vizinho not in self.listaVertices:
            nv = self.addVertice(vizinho)
        self.listaVertices[atual].addVizinho(self.listaVertices[vizinho], peso)

    def getVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())