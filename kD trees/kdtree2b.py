from kdtree1 import *

# поиск точек внутри окружности радиуса r с центром в точке p
def range_query_circular(t, p, r, found, depth=0):
    if t is None:
        return
    if kdcompare(t, Point(p.x-r, p.y-r), depth)>0:
        range_query_circular(t.right, p, r, found, depth+1)
        return
    if kdcompare(t, Point(p.x+r, p.y+r), depth)<0:
        range_query_circular(t.left, p, r, found, depth+1)
        return
    if p.distance(t.point) <= r:
        found.append(t.point)
        range_query_circular(t.left, p, r, found, depth+1)
        range_query_circular(t.right, p, r, found, depth+1)
        return

def test():
    data1 = [ (2,2), (0,5), (8,0), (9,8), (7,14),
    (13,12), (14,13) ]
    points = [Point(d[0], d[1]) for d in data1]
    p = Point(5,5)
    t1 = kdtree(points)
    found = []
    range_query_circular(t1, p, 5, found)
    print (found)

if __name__ == '__main__':
    test()