from math import inf
def inputGraphParams() -> list:
    ''' 
    Вводим параметры для таблицы графа узлы
    и количество соединений
    '''
    print('Enter value of nodes:')
    nodes: int
    nodes = int(input())
    graph = [[0]*nodes for _ in range(nodes)]
    return graph

def adjacencyTable(graph: list)->list:
    '''
    Заполняем таблицу смежности графа, вводя связи в алгебраическом виде
    Параметр "graph" - должен быть пустой матрицей смежности обрабатываемого графа
    '''
    status = True
    i: int
    j: int
    conn: str
    while status:
        print('Enter node connectctions and their weight (1Node,2Node,3Weight)\nExample: 1,2,3:')
        conn = input()
        if conn == '0':
            status=False
            continue
        i,j,weight=[int(x)-1 for x in conn.split(',')]
        graph[i][j] = weight+1
        graph[j][i] = weight+1
    return graph

def showGraph(graph: list)->None:
    """
    Показываем граф
    """
    for lines in graph:
        for cols in lines:
            print(f'{cols} ', end='')
        print('\n')

def get_linked_nodes(node, adjMatrix):
    """
    Возвращает генератор со связанными узлами
    """
    for i,weight in enumerate(adjMatrix[node]):
        if weight > 0:
            yield i


def get_next_node(weights, seen_nodes):
    """
    Возвращает следующую вершину, в зависимости от просмотренных вершин и их весов
    """
    next_node = -1
    min_weight = max(weights)
    #print(f" HERE {weights}")
    for i,weight in enumerate(weights):
        if weight < min_weight and i not in seen_nodes:
            min_weight = weight
            next_node = i
            #print("HERE",i)
    return next_node

def find_best_route(start,end):
    """
    Находит лучший маршрут, в зависимости от его последнего соеденения.
    То есть, допустим соеденения такие:
    | 0 | 1 | 2 | 3 | 4 |
    [ 0   0   3   4   0 ]
    И мы хотим дойти от 0 до 2
    Значит 2-3-4-0
    """
    route = [end]
    while end != start:
        end = links[route[-1]]
        route.append(end)
    for i,j in enumerate(route):
        route[i] = j+1
    return route

adjMatrix = inputGraphParams()
adjMatrix = adjacencyTable(adjMatrix)
node = 0
seen_nodes = [node]
weights = [inf]*len(adjMatrix[0])
weights[node] = 0
links = [0]*len(adjMatrix[0])

print(weights)
while node != -1:
    for j in get_linked_nodes(node,adjMatrix):
        if j not in seen_nodes:
            weight = weights[node] + adjMatrix[node][j]
            if weight < weights[j]:
                weights[j] = weight
                links[j] = node
    #print(weights)
    node = get_next_node(weights,seen_nodes)
    if node > 0:
        seen_nodes.append(node)
    
print('Adjacency table:')
showGraph(adjMatrix)

while True:
    print("Enter start of route")
    start = int(input())-1
    print("Enter end of route")
    end = int(input())-1
    print(f"The best route is: {find_best_route(start,end)}")

