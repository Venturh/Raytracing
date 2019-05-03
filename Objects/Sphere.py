import math
import numpy as np

class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center # point
        self.radius = radius # scalar
        self.material = material

    def __repr__(self):
        return 'Sphere(%s,%s)' % (repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = np.dot(co, ray.direction)
        discriminant = (v * v) - (np.dot(co, co) - self.radius*self.radius)
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        return (p - self.center) / np.linalg.norm(p - self.center)

    def getMaterial(self):
        return  self.material

