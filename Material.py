import numpy as np

class Material(object):

    def __init__(self,color):
        self.color = color
        self.ambient = 0.4
        self.diffuse = 0.4
        self.specular = 0.2
        self.surface = 32

    def colorAt(self,p):
        return self.color


class CheckerBoardMaterial(object):

    def __init__(self):
        self.black = np.array([255, 255, 255])
        self.white = np.array([0, 0, 0])
        self.ambient = 1
        self.diffuse = 0.6
        self.specular = 0.2
        self.surface = 32
        self.checkSize = 1

    def colorAt(self, p):
        v = p * (1.0 / self.checkSize)
        if (int(abs(v[0]) + 0.5) + int(abs(v[1]) + 0.5) + int(abs(v[2]) + 0.5)) % 2:
            return self.white
        return self.black
