import bisect  # Преобразование точек в проекцию Робинсона
from neville import *
from numpy import fabs

latitudes=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,
65, 70, 75, 80, 85, 90]

# длины параллелей на каждой широте в списке latitudes
A=[1.0000, 0.9986, 0.9954, 0.9900, 0.9822, 0.9730, 0.9600,
0.9427, 0.9216, 0.8962, 0.8679, 0.8350, 0.7986, 0.7597,
0.7186, 0.6732, 0.6213, 0.5722, 0.5322]

# расстояние от каждой параллели до экватора
# эти значения нужно умножать на 0.5072
B=[0.0000, 0.0620, 0.1240, 0.1860, 0.2480, 0.3100, 0.3720,
0.4340, 0.4958, 0.5571, 0.6176, 0.6769, 0.7346, 0.7903,
0.8435, 0.8936, 0.9394, 0.9761, 1.0000]

def find_le(a, x):
    """Находит самый правый элемент, меньший или равный x"""
    i = bisect.bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def get_interpolation_range(sidelen, n, i):
    """
    Находит диапазон индексов для интерполяции
    проекции Робинсона
    Вход
    sidelen: количество элементов по обе стороны от i,
    включая i в число левых
    n: общее число элементов
    i: индекс наибольшего элемента, меньшего значения
    Выход
    ileft: индекс левого значения (включая)
    iright: индекс правого значения (не включая)
    """
    if i<sidelen:
        ileft = max([0, i-sidelen+1])
    else:
        ileft = i-sidelen+1
        if i>=n-sidelen:
            iright = min(n, i+sidelen+1)
        else:
            iright = i+sidelen+1
    return ileft, iright

def transform1(lon, lat):
    """
    Возвращает результат преобразования lon и lat
    в координаты на проекции Робинсона.
    Вход
    lon: долгота
    lat: широта
    Выход
    x: координата x (начало координат в 0,0)
    y: координата y (начало координат в 0,0)
    """
    n = len(latitudes)
    south = False
    if lat<0:
        south = True
        lat = fabs(lat)
    if lat>90:
        return
    i = find_le(latitudes, lat)
    ileft, iright = get_interpolation_range(2, n, i)
    y = neville(latitudes[ileft:iright],
                B[ileft:iright], lat)
    if lat<=38:
        ileft, iright = get_interpolation_range(1, n, i)
    x = neville(latitudes[ileft:iright],
                A[ileft:iright], lat)
    y = 0.5072*y/2.0
    dx = x/360.0
    x = dx*lon
    if south:
        y = -1.0 * y
    return x, y, ileft, i, iright