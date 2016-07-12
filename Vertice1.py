class Vertice:
    """docstring for Vertice"""
    def __init__(self, chave):
        self.id = chave
        self.conexoes = {}

    def addVizinho(self, vizinho, peso=0):
        self.conexoes[vizinho] = peso

    def getConexoes(self):
        return self.conexoes.keys()

    def getID(self):
        return self.id

    def getPeso(self, vizinho):
        return self.conexoes[vizinho]