import numpy as np


class Triangle(object):

    def __init__(self, a, b, c, material):
        self.a = a
        self.b = b
        self.c = c
        self.u = b - a
        self.v = c - a
        self.material = material

    def __repr__(self):
        return 'Dreieck(%s, %s, %s)' %(repr(self.a), repr(self.b), repr(self.c))

    def intersectionParameter(self, strahl):
        w = strahl.ursprung - self.a
        dv = np.cross(strahl.richtung, self.v)
        dvu = np.dot(dv, self.u)
        if dvu == 0.0:
            return None
        wu = np.cross(w, self.u)
        r = np.dot(dv, w) / dvu
        s = np.dot(wu, strahl.richtung) / dvu
        if 0 <= r <= 1 and 0 <= s <= 1 and r+s <= 1:
            return np.dot(wu, self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        temp = np.cross(self.u, self.v)
        return temp / np.linalg.norm(temp)