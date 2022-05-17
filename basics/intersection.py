from line_segment import *
from sideplr import *

def getIntersectionPoint(s1, s2):
    """
    Вычисляет точку перечения отрезков s1 и s2.
    Предполагается, что s1 and s2 пересекаются.
    Факт пересечения необходимо проверить до вызова этой функции.
    """
    x1 = float(s1.lp0.x)
    y1 = float(s1.lp0.y)
    x2 = float(s1.rp.x)
    y2 = float(s1.rp.y)
    x3 = float(s2.lp0.x)
    y3 = float(s2.lp0.y)
    x4 = float(s2.rp.x)
    y4 = float(s2.rp.y)
    if s1.lp < s2.lp:
        x1,x2,y1,y2,x3,x4,y3,y4=x3,x4,y3,y4,x1,x2,y1,y2
    if x1 != x2:
        alpha1 = (y2-y1)/(x2-x1)
    if x3 != x4:
        alpha2 = (y4-y3)/(x4-x3)
    if x1 == x2: # s1 расположен вертикально
        y = alpha2*(x1-x3)+y3
        return Point([x1, y])
    if x3==x4: # s2 расположен вертикально
        y = alpha1*(x3-x1)+y1
        return Point([x3, y])
    if alpha1 == alpha2: # прямые параллельны
        return None
     # нужно вычислить
    x = (alpha1*x1-alpha2*x3+y3-y1)/(alpha1-alpha2)
    y = alpha1*(x-x1) + y1
    return Point(x, y)

def test_intersect(s1, s2):
    if s1==None or s2==None:
        return False
    # проверка: концы s2 лежат по одну сторону от s1
    lsign = sideplr(s2.lp0, s1.lp0, s1.rp)
    rsign = sideplr(s2.rp, s1.lp0, s1.rp)
    if lsign*rsign > 0:
        return False
    # проверка: концы s1 лежат по одну сторону от s2
    lsign = sideplr(s1.lp0, s2.lp0, s2.rp)
    rsign = sideplr(s1.rp, s2.lp0, s2.rp)
    if lsign*rsign > 0:
        return False
    return True

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(2, 1)
    p4 = Point(1, 4)
    s1 = Segment(0, p1, p2)
    s2 = Segment(1, p3, p4)
    s3 = Segment(2, p1, p2)
    if test_intersect(s1, s2):
        print(getIntersectionPoint(s1, s2))
        print(s1==s2)
        print(s1==s3)