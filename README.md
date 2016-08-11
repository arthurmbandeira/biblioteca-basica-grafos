# Biblioteca Básica de Grafos
## Descrição
Biblioteca implementada na linguagem Python para a disciplina de Algoritmos em Grafos.
Foram implementados as seguintes funções:
* Busca em Largura - BFS
* Busca em Profundidade - DFS
* Componentes Fortementes Conectados
* Caminho Mínimo - Bellman Ford

## Execução
O arquivo principal da biblioteca é o [lib.py](../master/lib.py) e deve ser executado com o seguinte comando:

``` $ python3 lib.py ```

Foram definidos alguns testes baseados nas notas de aula da disciplina e estes se encontram na pasta [testes](https://github.com/arthurmbandeira/biblioteca-basica-grafos/tree/master/testes).

O arquivo de teste deve estar no seguinte formato. A primeira linha informa o número de vértices do grafo, a segunda linha informa o número de arestas, a terceira linha informa se o grafo é direcionado ou não (0: não direcionado, 1: direcionado). Cada linha subsequente informa o par de vértices das arestas e o último elemento de cada linha indica o peso da aresta. Por exemplo: 

``` 
5
10
1
s t 6
s y 7
t x 5
t y 8
t z -4
x t -2
y x -3
y z 9
z s 2
z x 7 
```

Quando solicitado pelo programa, insira o nome do arquivo presente na pasta testes com a extensão, por exemplo:

``` teste_bfs.txt ```

Após isso siga as orientações do menu apresentado no console.

### Arthur Manuel Bandeira
