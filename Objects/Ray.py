class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction  # laenge 1


    def intersectionParameter(self, t):
        return self.origin + self.direction.scale(t)

    def __repr__(self):
        return 'Ray(%s,%s)' %(repr(self.origin),repr(self.direction))