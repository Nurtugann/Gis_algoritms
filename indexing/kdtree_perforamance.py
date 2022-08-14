from kdtree1 import *
from prkdtree1 import *

import random
import time
import sys
import string

if __name__ == '__main__':
    npts = 1000 # число точек по умолчанию
    if len(sys.argv)==2: # заданное пользователем число точек
        if sys.argv[1].isdigit() is True:
            npts = string.atoi(sys.argv[1])
    points = []
    for i in range(npts):
        p = Point(random.random(), random.random())
        points.append(p)    
    time1 = time.time()
    kdt1 = kdtree(points)
    time2 = time.time()
    treet1 = time2-time1    
    time1 = time.time()
    kdt2 = kdtree2(points)
    time2 = time.time()
    treet2 = time2-time1    
    px = [p.x for p in points]
    py = [p.y for p in points]
    xmin = min(px)
    xmax = max(px)
    ymin = min(py)
    ymax = max(py)
    xylim = [ [xmin, xmax], [ymin, ymax] ]
    time1 = time.time()
    kdt3 = prkdtree(points, xylim)
    time2 = time.time()
    treet3 = time2-time1    
    print (npts, "|", treet1, treet2, treet3, "|",   )
    n = 100
    t1 = 0 # время поиска 100 точек в kd-дереве
    t2 = 0 # время поиска в сбалансированном kd-дереве
    t3 = 0 # время поиска в точечно-регионном kd-дереве
    t4 = 0 # время линейного поиска
    pp = random.sample(points, n)
    for p in pp:
        time1 = time.time()
        p1 = query_kdtree(kdt1, p)
        time2 = time.time()
        t1 = t1 + time2-time1   
        time1 = time.time()
        p1 = query_kdtree(kdt2, p)
        time2 = time.time()
        t2 = t2 + time2-time1   
        time1 = time.time()
        p1 = query_prkdtree(kdt3, p)
        time2 = time.time()
        t3 = t3 + time2-time1   
        time1 = time.time()
        for i in range(len(points)):
            if p == points[i]:
                break
        time2 = time.time()
        t4 = t4 + time2-time1   
    print (t1, t2, t3, t4)