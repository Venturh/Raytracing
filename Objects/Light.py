

class Light(object):
    def __init__(self,origin, color):
        self.origin = origin
        self.color = color

    def dist(self ,ray):
        return self.origin - ray.origin/ray.direction

