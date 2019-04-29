class Plane(object):

    def __init__(self, point, normal,material):
        self.point = point  # point
        self.normal = normal  # vector
        self.material = material

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

    def normalAt(self, p):
        return self.normal

    def getMaterial(self):
        return self.material