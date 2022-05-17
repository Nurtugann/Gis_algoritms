import sys
sys.path.append(r'C:\Users\User\Desktop\4 semester\GIS\basics')
from point import *

class PQuadTreeNode():
    def __init__(self,point,nw=None,ne=None,se=None,sw=None):
        self.point = point
        self.nw = nw
        self.ne = ne
        self.se = se
        self.sw = sw
    def __repr__(self):
        return str(self.point)
    def is_leaf(self):
        return self.nw==None and self.ne==None and \
            self.se==None and self.sw==None

def search_pqtree(q, p, is_find_only=True):
    if q is None:
        return
    if q.point == p:
        if is_find_only:
            return q
        else:
            return
    dx,dy = 0,0
    if p.x >= q.point.x:
        dx = 1
    if p.y >= q.point.y:
        dy = 1
    qnum = dx+dy*2
    child = [q.sw, q.se, q.nw, q.ne][qnum]
    if child is None and not is_find_only:
        return q
    return search_pqtree(child, p, is_find_only)

def insert_pqtree(q, p):
    n = search_pqtree(q, p, False)
    node = PQuadTreeNode(point=p)
    if p.x < n.point.x and p.y < n.point.y:
        n.sw = node
    elif p.x < n.point.x and p.y >= n.point.y:
        n.nw = node
    elif p.x >= n.point.x and p.y < n.point.y:
        n.se = node
    else:
        n.ne = node

def pointquadtree(data):
    root = PQuadTreeNode(point = data[0])
    for p in data[1:]:
        insert_pqtree(root, p)
    return root

if __name__ == '__main__':
    data1 = [ (2,2), (0,5), (8,0), (9,8), (7,14),
    (13,12), (14,13) ]
    points = ([Point(d[0], d[1]) for d in data1])
    q = pointquadtree(points)
    print ([search_pqtree(q, p) for p in points])