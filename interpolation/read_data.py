def read_data(fname):
    """
    Читает данные из файла. В каждой строке должно быть три столбца:
    X, Y и Значение.
    Вход
    fname: путь к файлу
    Выход
    x3: список списков размерности 3×n
    Каждый внутренний список содержит 3 элемента: X, Y, Значение
    """
    f = open(fname, 'r')
    x1 = f.readlines()
    x2 = [x.strip().split() for x in x1]
    x3 = [[float(x[0]),float(x[1]),float(x[2])] for x in x2]
    return x3