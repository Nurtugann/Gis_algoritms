from network2listmatrix import network2list
def dfs(network, v):
    """
    Поиск в глубину
    Вход
    network: сеть, представленная списком списков
    v: узел, с которого начинается поиск
    Выход
    V: список посещенных узлов
    """
    n = len(network)
    S = [] # пустой стек
    S.append(v)
    V = []
    labelled = [ False for i in range(n)]
    labelled[v] = True
    while len(S) > 0:
        print (S)
        t = S.pop()
        V.append(t)
        for u in network[t]:
            if not labelled[u]:
                labelled[u] = True
                S.append(u)
    return V
if __name__ == "__main__":
    network = network2list('network-links')
    V = dfs(network, 3)
    print ("Посещенные:", V)