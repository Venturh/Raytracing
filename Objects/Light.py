

class Light(object):
    def __init__(self,origin, color):
        self.origin = origin
        self.color = color

    def distance(self, ray):
        return self.origin[0] - ray.origin[0]/ray.direction[0]

