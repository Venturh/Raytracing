class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction  # laenge 1

    def punktbeiparameter(self, t):
        return self.origin + self.direction * t

    def __repr__(self):
        return 'Ray(%s,%s)' %(repr(self.origin),repr(self.direction))


class Plane(object):

    def __init__(self, point, normal):
        self.point = point  # point
        self.normal = normal  # vector

    def __repr__(self):
        return 'Plane(%s,%s)' % (repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)
        if b:
            return -a / b
        else:
            return None
