class Phong(object):

    def __init__(self, color):
        self.color = color
        self.ambientKoeffizient = 0.4
        self.diffuseKoeffizient = 0.4
        self.spekularKoeffizient = 0.2
        self.oberflaeche = 32

    def colorAt(self,z):
        return self.color
