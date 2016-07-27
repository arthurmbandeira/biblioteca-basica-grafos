#Arthur Manuel Bandeira - RA 67226

import heapq

from Grafo import Grafo
from DFS import *
from BFS import *
from SCC import *
from bellmanFord import *

G = Grafo()

def ler(G, file, direcionado):
    line = file.readline()
    spt = line.split()
    x = (spt[0])
    y = (spt[1])
    z = int(spt[2])
    if (not direcionado):
        G.addAresta(x, y, z)
        G.addAresta(y, x, z)
    else:
        G.addAresta(x, y, z)
    return G

def imprimeGrafo(G):
    for v in G:
        for w in v.getAdj():
            print(v.getID(), w.getID(), v.getPeso(w))
    print('\n')

def abreArquivo(path):
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        print("Arquivo inexistente ou inacessivel na pasta testes, tente novamente...")
        interfaceArquivo()
        return

    nroVertices = int(f.readline())
    nroArestas = int(f.readline())
    direcionado = int(f.readline())
    for i in range(nroArestas):
        ler(G, f, direcionado)

    f.close()

def interfaceArquivo():
    arquivo = input("Digite o nome do arquivo de entrada (deve estar na pasta testes): ")
    arquivo = "testes/" + str(arquivo) + ".txt"
    abreArquivo(arquivo)

def menu():
    print('\n')
    print("Escolha uma das opcoes ou pressione 'q' para sair")
    print("[1] Busca em Largura")
    print("[2] Busca em Profundidade")
    print("[3] Componentes Fortementes Conectados")
    print("[4] Caminho Minimo - Bellman Ford")
    print("[5] Imprimir Grafo")
    print("[6] Trocar arquivo")
    print("[q] Sair")

print('\n')
print("0000000000000000000000000000000000000000000000000000000000000000000000000000")
print("00************************************************************************00")
print("00******************    Biblioteca Basica de Grafos     ******************00")
print("00************************************************************************00")
print("0000000000000000000000000000000000000000000000000000000000000000000000000000")
print('\n')

interfaceArquivo()
menu()
while True:
    teclado = input()
    if teclado == '1':
        s = input("Informe o vertice inicial: ")
        print('\n')
        if s not in G.getVertices():
            print("Este vertice nao pertence ao grafo, tente novamente.")
        else:
            bfs(G, s)
    elif teclado == '2':
        s = input("Informe o vertice inicial: ")
        print('\n')
        if s not in G.getVertices():
            print("Este vertice nao pertence ao grafo, tente novamente.")
        else:
            dfs(G, s)
    elif teclado == '3':
        s = input("Informe o vertice inicial: ")
        print('\n')
        if s not in G.getVertices():
            print("Este vertice nao pertence ao grafo, tente novamente.")
        else:
            scc(G, s)
    elif teclado == '4':
        s = input("Informe o vertice inicial: ")
        t = input("Informe o vertice destino: ")
        print('\n')
        if s not in G.getVertices():
            print("O vertice inicial nao pertence ao grafo, tente novamente.")
        else:
            caminhoBF(G, s, t)
    elif teclado == '5':
        imprimeGrafo(G)
    elif teclado == '6':
        del G
        G = Grafo()
        interfaceArquivo()
        imprimeGrafo(G)
    elif teclado == 'q':
        print("Tchau!")
        break
    else:
        menu()