from kdtree1 import *

def range_query_orthogonal(t, rect, found, depth=0):
    if t is None:
        return
    k = len(t.point)
    axis = depth%k
    if t.point[axis] < rect[0][axis]:
        range_query_orthogonal(t.right, rect, found, depth+1)
        return
    if t.point[axis] > rect[1][axis]:
        range_query_orthogonal(t.left, rect, found, depth+1)
        return
    x, y = t.point.x, t.point.y
    if not (rect[0][0]>x or rect[0][1]>y or rect[1][0]<x or rect[1][1]<y):
        found.append(t.point)
    range_query_orthogonal(t.left, rect, found, depth+1)
    range_query_orthogonal(t.right, rect, found, depth+1)
    return

def test():
    data1 = [ (2,2), (0,5), (8,0), (9,8), (7,14), (13,12), (14,13) ]
    points = [Point(d[0], d[1]) for d in data1]
    t1 = kdtree(points)
    rect = [ [1, 2], [9, 9] ] # searching points between (1,2) and (9,9)
    found = []
    range_query_orthogonal(t1, rect, found)
    print (found)

if __name__ == '__main__':
    test()