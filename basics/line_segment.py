from point import *
from sideplr import *

## Два статуса левого конца
ENDPOINT = 0 ## изначальный левый конец
INTERIOR = 1 ## внутренняя точка отрезка

class Segment:
    """
    Класс для представления отрезков прямых.
    """
    def __init__(self, e, p0, p1, c=None):
        """
        Конструктор класса Segment.
        Вход
        e: ИД отрезка, целое число
        p0, p1: концы отрезка, объекты Point 
        """
        if p0>=p1:
            p0,p1 = p1,p0 # p0 всегда левый конец
        self.edge = e # ИД, задается для всех сторон
        self.lp = p0 # левый конец
        self.lp0 = p0 # первоначальный левый конец
        self.rp = p1 # правый конец
        self.status = ENDPOINT # статус отрезка
        self.c = c # c: ИД свойства
    def __eq__(self, other):
        if isinstance(other, Segment):
            return (self.lp==other.lp and self.rp==other.rp) or (self.lp==other.rp and self.rp==other.lp)
        return NotImplemented
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    def __lt__(self, other): # self < other ?
        if isinstance(other, Segment):
            if self.lp and other.lp:
                lr = sideplr(self.lp, other.lp, other.rp)
                if lr == 0:
                    lrr = sideplr(self.rp, other.lp, other.rp)
                    if other.lp.x < other.rp.x:
                        return lrr > 0
                    else:
                        return lrr < 0
                else:                           #                   (+) -----> (self) (false)
                    if other.lp.x > other.rp.x: #                   <------ (other segment)
                        return lr < 0           #                   (-)   -----> (self) (true)      (-) <------ (self) (false)
                    else:                       #                                               ------> (other segment)
                        return lr > 0           #                                                   (+)  <------ (self) (true)
        return NotImplemented
    def __gt__(self, other):
        result = self.__lt__(other)
        if result is NotImplemented:
            return result
        return not result
    def __repr__(self):
        return "{0}".format(self.edge)
    def contains(self, p):
        """
        Возвращает True, если точка p является концом отрезка
        """
        if self.lp == p:
            return -1
        elif self.rp == p:
            return 1
        else:
            return 0