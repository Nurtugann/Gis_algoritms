import numpy as np

class Quad():
    def __init__(self, value, dim, nw, ne, se, sw):
        self.value = value
        self.dim = dim
        self.nw = nw
        self.ne = ne
        self.se = se
        self.sw = sw
    def __repr__(self):
        return str(self.value)

def homogeneity(d):
    v = d[0,0]
    for i in d:
        for j in i:
            if j != v:
                return False
    return True

def quadtree(data):
    dim = data.shape[0]
    dim2 = int(dim/2)
    if homogeneity(data) is True:
        return Quad(value=data[0,0], dim=dim, nw=None, ne=None, se=None, sw=None)
    return Quad(value=None,
    dim = dim,
    nw = quadtree(data[0:dim2, 0:dim2]),
    ne = quadtree(data[0:dim2, dim2:,]),
    se = quadtree(data[dim2:,dim2:,]),
    sw = quadtree(data[dim2:,0:dim2]))

#############################################################
# Примечание: x, y отсчитываются от левого верхнего угла
#
# Квадранты в дочерних узлах расположены в порядке
# [q.nw, q.ne, q.sw, q.se]. Ячейка, в которую попадает (x, y) в
# каждом регионе, определяется значениями dx и dy. Тогда квадрант,
# в котором расположена (x, y), вычисляется по формуле dx + dy * 2.
#
# dx
#
# ----+-----+------
# | 0 | 1
# ----+-----+------
# dy 0 | 0 | 1
# ----+-----+------
# 1 | 3 | 2
# ----+-----+------
#
#############################################################
def query_quadtree(q, x, y):
    if q.value is not None: # это листовой узел
        return q.value # вернуть значение
    dim = q.dim
    dim2 = dim/2
    dx,dy = 0, 0
    if x>=dim2:
        dx = 1
        x = x-dim2
    if y>=dim2:
        dy = 1
        y = y-dim2
    qnum = dx+dy*2
    return query_quadtree([q.nw,q.ne,q.sw,q.se][qnum], x, y)

def test():
    data0 = np.array(
    [[0, 1, 2, 2],
    [2, 2, 2, 2],
    [0, 0, 2, 0],
    [0, 0, 1, 0]])

    data1 = np.array(
    [[0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0],
    [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1]])

    q = quadtree(data1)
    for y in range(q.dim):
        for x in range(q.dim):
            print (query_quadtree(q, x, y), end='')
        print()
    return q

if __name__ == '__main__':
    test()