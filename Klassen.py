class Ray(object):
    def __init__(self, ursprung, richtung):
        self.origin = ursprung
        self.direction = richtung  # laenge 1

    def punktbeiparameter(self, t):
        return self.ursprung + self.richtung.scale(t)


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
