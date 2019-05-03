import numpy as np


class Plane(object):
    def __init__(self, point, normal,material):
        self.point = point  # point
        self.normal = normal / np.linalg.norm(normal)
        self.material = material

    def __repr__(self):
        return 'Plane(%s,%s)' % (repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        op = ray.origin - self.point
        a = np.dot(op, self.normal)
        b = np.dot(ray.direction, self.normal)
        if b:
            temp = -(a / b)
            if temp > 0:
                return -(a/b)
            else:
                return None
        else:
            return None

    def normalAt(self, p):
        return self.normal

    def getMaterial(self):
        return self.material
