from network2listmatrix import network2list
def bfs(network, v):
    """
    Поиск в ширину
    Вход
    network: сеть, представленная списком списков
    v: узел, с которого начинается поиск
    Выход
    V: список посещенных узлов
    """
    n = len(network)
    Q = []
    Q.append(v)
    V = []
    labeled = [ False for i in range(n)]
    labeled[v] = True
    while len(Q) > 0:
        print(Q)
        # печатать list(Q)
        t = Q.pop(0)
        V.append(t)
        for u in network[t]:
            if not labeled[u]:
                labeled[u] = True
                Q.append(u)
    return V
if __name__ == "__main__":
    network = network2list('network-links')
    V = bfs(network, 3)
    print ("Посещенные:", V)