from point import *

def sideplr(p, p1, p2):
    """
    Вычисляет, по какую сторону от вектора p1p2 находится точка p.
    Вход
    p: точка
    p1, p2: начало и конец вектора
    Выход
    -1: p слева p1p2
    0: p на прямой p1p2
    1: p справа p1p2
    """
    return int((p.x-p1.x)*(p2.y-p1.y)-(p2.x-p1.x)*(p.y-p1.y))

if __name__ == "__main__":
    p=Point(1,1)
    p1=Point(0,0)
    p2=Point(1,0)
    print ("Положение точки %s относительно прямой %s->%s: %d"%(
    p, p1, p2, sideplr(p, p1, p2)))
    print ("Положение точки %s относительно прямой %s->%s: %d"%(
    p, p2, p1, sideplr(p, p2, p1)))
    p = Point(0.5, 0)
    print ("Положение точки %s относительно прямой %s->%s: %d"%(
    p, p1, p2, sideplr(p, p1, p2)))
    print ("Положение точки %s относительно прямой %s->%s: %d"%(
    p, p2, p1, sideplr(p, p2, p1)))