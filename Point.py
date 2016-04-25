from math import hypot
from random import randint
class Point:
    _rangeX = (-10,10)
    _rangeY = (-10,10)
    def __init__(self, x = -100, y = -100):
        self._x = randint(self._rangeX[0], self._rangeX[1]) if x == -100 else x
        self._y = randint(self._rangeY[0], self._rangeY[1]) if y == -100 else y

    def __repr__(self):
        return "({0},{1})".format(self._x, self._y)
    def __str__(self):
        return "({0},{1})".format(self._x, self._y)
    def __lt__(self, other):
        return self.y() < other.y() if self.x() == other.x() else self.x() < other.x()
    def __eq__(self, other):
        return self.x() == other.x() and self.y() == other.y()
    def __ne__(self, other):
        return not self == other
    def __hash__(self):
        return hash((self.x(), self.y()))
        
    def x(self):
        return self._x
    def y(self):
        return self._y

    def dist(self, other):
        return hypot(other.x() - self.x(), other.y() - self.y())
    def orientation(self, q, r):
        ''' Returns positive number if p-q-r are clockwise, neg if ccw, 0 if collinear'''
        return (q.y() - self.y()) * (r.x() - self.x()) - (q.x() - self.x()) * (r.y() - self.y())
