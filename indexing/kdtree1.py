import sys
sys.path.append('basics')
from point import *

class kDTreeNode():
    def __init__(self, point, left, right):
        self.point = point
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.point)
def kdcompare(r, p, depth):
    """
    Возвращает результат поиска в kd-дереве
    Вход
    r: корень
    p: точка
    depth : начальная глубина поиска
    Выход
    –1 (идти по левой ветви) или 1 (идти по правой ветви)
    """
    k = len(p)
    dim = depth % k
    if p[dim] <= r.point[dim]:
        return -1
    else:
        return 1
        
def kdtree(points):
    """
    Создает kd-дерево, содержащее точки в заданном порядке
    """
    root = kDTreeNode(point=points[0], left=None, right=None)
    for p in points[1:]:
        node = kDTreeNode(point=p, left=None, right=None)
        p0, lr = query_kdtree(root, p, 0, False)
        if lr<0:
            p0.left = node
        else:
            p0.right = node
    return root

def query_kdtree(t, p, depth=0, is_find_only=True):
    if t is None:
        return
    if t.point == p and is_find_only:
        return t
    lr = kdcompare(t, p, depth)
    if lr<0:
        child = t.left
    else:
        child = t.right
    if child is None:
        if not is_find_only:
            return t, lr
        else:
            return
    return query_kdtree(child, p, depth+1, is_find_only)

# всегда использует медианную точку для разбиения данных на две части
def kdtree2(points, depth = 0):
    if len(points)==0:
        return
    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda points: points[axis])
    pivot = len(points)//2
    while pivot<len(points)-1 and points[pivot][axis]==points[pivot+1][axis]:
        pivot += 1
    return kDTreeNode(point=points[pivot], left=kdtree2(points[:pivot], depth+1), right=kdtree2(points[pivot+1:], depth+1))

if __name__ == '__main__':
    data1 = [ (2,2), (0,5), (8,0), (9,8),
    (7,14), (13,12), (14,13) ]
    points = [Point(d[0], d[1]) for d in data1]
    p = points[0]
    t1 = kdtree(points)
    t2 = kdtree2(points)
    print ([query_kdtree(t1, p) for p in points ])
    print ([query_kdtree(t2, p) for p in points ])