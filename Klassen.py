

class Light(object):

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def abstand(self, ray):
        return (self.position[0] - ray.origin[0]) / ray.direction[0]
