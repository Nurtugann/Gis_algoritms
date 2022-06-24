INF = float('inf')

def network2list(fname, is_zero_based = True):
    """
    Преобразовать файл сети в списковую структуру данных.
    Вход
    fname: имя файла сети, записанного в формате:
    n
    i j расстояние
    ...
    Выход
    network: список списков, в котором i-й элемент содержит список
    всех узлов, смежных с узлом i
    """
    f = open(fname)
    l = f.readline()
    n = int(l.strip().split()[0])
    network = [[] for i in range(n)]
    for l in f:
        nodesnedge = l.strip().split()
        if len(nodesnedge)==3:
            i=int(nodesnedge[0])
            j=int(nodesnedge[1])
            if not is_zero_based:
                i = i-1
                j = j-1
            network[i].append(j)
            network[j].append(i)
    f.close()
    return network

def network2distancematrix(fname, is_zero_based = True):
    """
    Читает список из входного файла и возвращает матрицу
    смежности. Входной файл содержит n + 1 строк и должен быть
    записан в следующем формате:

    i j расстояние
    ...

    где первая строка содержит число ребер, а каждая
    из последующих – индексы вершин ребра и расстояние,
    ассоциированное с этим ребром. Нумерация индексов
    начинается с 0 (по умолчанию) или с 1.
    """
    a = []
    f = open(fname)
    l = f.readline()
    n = int(l.strip().split()[0])  # число ребер
    a=[[INF]*n for x in range(n)]  # инициализировать 2-мерный список INF
    for l in f:
        nodesnedge = l.strip().split()
        if len(nodesnedge)==3:
            i=int(nodesnedge[0])
            j=int(nodesnedge[1])
            if not is_zero_based:
                i = i-1
                j = j-1
            d=int(nodesnedge[2])
            a[i][j] = d
            a[j][i] = d
    for i in range(n):
        a[i][i] = 0
    return a

