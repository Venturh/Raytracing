import numpy as np
import math


from Objects.Ray import Ray


class Camera(object):

    def __init__(self, e, c, up, fov, aspectratio, wres, hres):
        self.e = e
        self.f = (c - e) / np.linalg.norm(c - e)
        self.s = np.cross(self.f, up) / np.linalg.norm(np.cross(self.f, up))
        self.u = np.cross(self.s, self.f)
        self.alpha = fov / 2
        self.height = 2 * math.tan(self.alpha)
        self.width = aspectratio * self.height
        self.pixelwidth = self.width / (wres - 1)
        self.pixelheight = self.height / (hres - 1)

    def calcray(self, x, y):
        xcomp = self.s * (x * self.pixelwidth - self.width / 2)
        ycomp = self.u * (y * self.pixelheight - self.height / 2)
        return Ray(self.e, self.f + xcomp + ycomp)


