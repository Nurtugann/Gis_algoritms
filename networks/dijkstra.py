

INF = float('inf')

# from network2listmatrix import *

def dijkstra(source, distmatrix):
    """
    Алгоритм Дейкстры поиска кратчайших путей из одного узла.
    Вход
    source: индекс начального узла
    distmatrix: матрица расстояний, элемент (i, j) равен INF,
    если узлы i и j не соединены ребром, иначе
    элемент равен весу (длине) этого ребра
    Выход
    dist: полные расстояния от начального узла до всех остальных
    prev: список, в котором для каждого узла указан предшествующий ему
    на кратчайшем пути
    """
    n = len(distmatrix)
    dist = [INF if i!=source else 0 for i in range(n)]
    prev = [None for i in range(n)]
    Q = list(range(n))
    while len(Q)>0:
        u = get_remove_min(Q, dist)
        U = get_neighbor(u, distmatrix, n)
        for v in U:
            newd = dist[u] + distmatrix[u][v]
            if newd < dist[v]:
                dist[v] = newd
                prev[v] = u
    return dist, prev

def get_remove_min(Q, dist):
    """
    Находит в Q узел с наименьшим расстоянием в dist и удаляет
    этот узел из Q.
    Вход
    Q: список узлов-кандидатов
    dist: список расстояний от каждого узла до начального
    Выход
    imin: индекс узла с наименьшим расстоянием
    """
    dmin = INF
    imin = -1
    for i in Q:
        if dist[i] < dmin:
            dmin = dist[i]
            imin = i
    Q.remove(imin)
    return imin

def get_neighbor(u, d, n):
    neighbors = [i for i in range(n)
                 if d[i][u]!=INF and i!=u]
    return neighbors

def shortest_path(source, destination, distmatrix):
    dist, prev = dijkstra(source, distmatrix)
    last = prev[destination]
    path = [destination]
    while last is not None:
        path.append(last)
        last = prev[last]
    return path, dist[destination]


if __name__ == "__main__":
    from network2listmatrix import *
    fname = 'network-links'
    a = network2distancematrix(fname, True)
    print(shortest_path(1, 6, a))
    print(shortest_path(0, 7, a))
    