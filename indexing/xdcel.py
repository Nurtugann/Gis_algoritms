import sys
sys.path.append('basics')
from extent import *
from dcel import *

class Edge:
    """Ребро в топологически связанном пространственном наборе данных"""
    def __init__(self, v1, v2, leftpoly, rightpoly):
        # Начало определяется как вершина, в которую ведет ребро
        self.fr = v1
        self.to = v2
        self.left = leftpoly
        self.right = rightpoly
    def __eq__(self, other): # v1->v2 is eq. to v2->v1
        return (self.fr == other.fr and self.to == other.to)\
        or (self.fr == other.to and self.to == other.fr)
    def extent(self):
        xmin = min(self.fr.x, self.to.x)
        xmax = max(self.fr.x, self.to.x)
        ymin = min(self.fr.y, self.to.y)
        ymax = max(self.fr.y, self.to.y)
        return Extent(xmin, xmax, ymin, ymax)
    def is_endpoint(self, p):
        if p == self.fr or p==self.to:
            return True
        return False
    def __repr__(self):
        return "{0}->{1}".format(self.fr, self.to)
class Xdcel(Dcel):
    def __init__(self, D):
        Dcel.hedges = D.hedges
        Dcel.vertices = D.vertices
        Dcel.faces = D.faces
        self.edges=[]
        self.build_xdcel()
    def build_xdcel(self):
        """Построить объекты Edge по информации, хранящейся в ДСР"""
        if not len(self.vertices) or not len(self.hedges):
            return
        for h in self.hedges:
            v1 = h.origin
            v2 = h.nexthedge.origin
            lf = h.face
            rf = h.twin.face
        e = Edge(v1, v2, lf, rf)
        try:
            i = self.edges.index(e)
        except ValueError:
            i = None
        if i is None:
            self.edges.append(e)