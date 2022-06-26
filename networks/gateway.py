from network2listmatrix import *
from dijkstra import shortest_path

def gateway(s1, s2, gatewaynode, distmatrix):
    """
    Находит кратчайший путь, проходящий через калитку.
    Вход
    s1: первый конец пути
    s2: второй конец пути
    gatewaynode: узел-калитка
    Выход
    Список узлов на пути и полный вес пути
    """
    path1, d1 = shortest_path(s1, gatewaynode, distmatrix)
    path2, d2 = shortest_path(s2, gatewaynode, distmatrix)
    path1.reverse()
    return path1[:-1]+path2, d1+d2
if __name__ == "__main__":
    fname = 'network-links'
    a = network2distancematrix(fname, True)
    print (gateway(0, 7, 2, a))