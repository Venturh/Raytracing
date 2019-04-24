class Ray(object):
    def __init__(self, ursprung, richtung):
        self.ursprung = ursprung
        self.richtung = richtung.normalized()  # laenge 1

    def punktbeiparameter(self, t):
        return self.ursprung + self.richtung.scale(t)
