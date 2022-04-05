import ogr   # Тестирование проекции Робинсона
import matplotlib.pyplot as plt
from transform1 import *
from worldmap import *

fname = '../data/ne_110m_coastline.shp'
pp, numgraticule, numline = prep_projection_data(fname)

points=[]
for p in pp:
    p1 = transform1(p[1], p[2])
    points.append([p[0], p1[0], p1[1]])

for i in range(numline):
    if i<numgraticule:
        col = 'lightgrey'
    else:
        col = '#5a5a5a'
    ptsx = [p[1] for p in points if p[0]==i]
    ptsy = [p[2] for p in points if p[0]==i]
    plt.plot(ptsx, ptsy, color=col)

plt.axis('scaled')
frame = plt.gca()
frame.axes.get_xaxis().set_visible(False)
frame.axes.get_yaxis().set_visible(False)
frame.set_frame_on(False)
#plt.savefig(robinson.eps',bbox_inches='tight',pad_inches=0)
frame.set_frame_on(True)
plt.show()