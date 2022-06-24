from network2listmatrix import network2distancematrix
def allpairs(a):
    """
    Возвращает матрицу весов (расстояний) для нахождения кратчайших
    путей между всеми парами узлов по алгоритму Флойда–Уоршелла.
    Вход
    a: начальная матрица расстояний, в которой расстояния между
    всеми несмежными парами узлов равны бесконечности.
    Выход
    Функция модифицирует переданную на вход матрицу.
    """
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][j] > a[i][k]+a[k][j]:
                    a[i][j] = a[i][k]+a[k][j]
if __name__ == "__main__":
    fname = 'network-links'
    a = network2distancematrix(fname, True)
    allpairs(a)
    print (a[1][6])
    print (a[0][7])