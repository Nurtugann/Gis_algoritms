def neville(datax, datay, x):
    """
    Находит интерполированное значение с помощью алгоритма Невилла.
    Вход
    datax: входные x в списке длины n
    datay: входные y в списке длины n
    x: точка, в которой ищется интерполированное значение
    Выход
    p[0]: полином степени n
    """
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i] + (datax[i]-x)*p[i+1]) / (datax[i]-datax[i+k])
    return p[0]