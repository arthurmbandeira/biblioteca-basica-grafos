''' Respresentação de um Grafo por lista de adjacência utilizando dicionários padrão da linguagem '''

from Vertice import Vertice
from collections import OrderedDict

class Grafo:
    '''Classe que representa um grafo'''
    def __init__(self):
        self.listaVertices = OrderedDict() # Lista de Vertices
        self.numVertices = 0 # Numero de vertices
        self.topologicalSort = [] # Ordenação topológica do grafo

    # Método que adiciona vértices no grafo
    def addVertice(self, chave):
        self.numVertices += 1
        novoVertice = Vertice(chave)
        self.listaVertices[chave] = novoVertice
        return novoVertice

    # Método que ao receber uma chave v, retorna o vértice v do grafo
    def getVertice(self, v):
        if v in self.listaVertices:
            return self.listaVertices[v]
        else:
            return None

    # Método que adiciona arestas no grafo
    def addAresta(self, atual, vizinho, peso = 0):
        if atual not in self.listaVertices:
            nv = self.addVertice(atual)
        if vizinho not in self.listaVertices:
            nv = self.addVertice(vizinho)
        self.listaVertices[atual].addVizinho(self.listaVertices[vizinho], peso)

    # Método que retorna os vértices do grafo
    def getVertices(self):
        return self.listaVertices.keys()

    # Método "mágico" de Python para que o grafo seja iterável
    def __iter__(self):
        return iter(self.listaVertices.values())