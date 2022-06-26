from locale import atoi
import sys
sys.path.append('networks')
from network2listmatrix import network2distancematrix
from allpairdist import allpairs




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

X = [['']*n for i in range(n)]
for i in range(n):
    for j in range(n):
        X[i][j] = 'x_%d_%d'%(i, j)
# целевая функция
obj='MIN: '
for i in range(n):
    for j in range(n):
        obj += "%d"%(a[i][j])+"*"+X[i][j] # %f, если числа вещественные
        if not (i == n-1 and j == n-1):
            obj += '+'
        else:
            obj=obj+';'
# ограничения
con1 = ['' for i in range(n)]
for i in range(n):
    con1[i] = X[i][0]
    for j in range(1,n):
        con1[i] += '+'+X[i][j]
    con1[i] += '=1;'

con2 = X[0][0]
for j in range(1, n):
    con2 += '+'+X[j][j]
con2 += '=%d;'%(p)
con3 = []
for i in range(n):
    for j in range(n):
        if i != j:
            con3.append(X[i][j] + '-' + X[j][j] + '<=0;')

con4 = 'BIN '
for i in range(n):
    for j in range(n):
        con4 += X[i][j]
        if not (i == n-1 and j == n-1):
            con4 += ','
        else:
            con4 += ';'
# распечатать
print (obj)
for i in range(n):
    print (con1[i])

print (con2)
for i in range(len(con3)):
    print (con3[i])
print (con4)