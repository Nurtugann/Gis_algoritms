import sys
from locale import atoi
sys.path.append('networks')
from network2listmatrix import network2distancematrix
from allpairdist import allpairs
INF = float('inf')
def evaluate(dist, median, n):
    sumdist = 0.0
    p = len(median)
    for i in range(n):
        dist0 = INF
        for j in range(p):
            if dist[i][median[j]] < dist0:
                dist0 = dist[i][median[j]]
        sumdist += dist0
    return sumdist
if len(sys.argv) <=1:
    print (sys.argv[0], "filename [ [True|False] p]")
    sys.exit()
zerobased = True
p = 2
if len(sys.argv)>=3 and sys.argv[2]=="False":
    zerobased = False
if len(sys.argv)>=4:
    p = atoi(sys.argv[3])
a = network2distancematrix(sys.argv[1], zerobased)
allpairs(a)
n = len(a)
median = []
candidates = [i for i in range(n)]
for j in range(p):
    dmin = INF
    imin = -1
    for i in candidates:
        d = evaluate(a, median+[i], n)
        if d < dmin:
            dmin = d
            imin = i
    candidates.remove(imin)
    median.append(imin)
print (median, dmin)