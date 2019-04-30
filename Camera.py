import numpy as np
import math


from Objects.Ray import Ray


class Camera(object):
    f = np.array([0, 0, 0])
    s = np.array([0, 0, 0])
    u = np.array([0, 0, 0])

    def __init__(self, e, c, up, aspectratio, fieldofview, wres, hres, objectlist, image, backgroundcolor):
        self.e = e
        self.c = c
        self.up = up
        self.aspectratio = aspectratio
        self.fieldofview = fieldofview
        self.wres = wres
        self.hres = hres
        self.objectlist = objectlist
        self.image = image
        self.backgroundcolor = backgroundcolor

        self.f = self.c-self.e / np.linalg.norm(c - e)
        self.s = np.cross(self.f, self.up) / np.linalg.norm(np.cross(self.f, self.up))
        self.u = np.cross(self.f, self.s)

        self.alpha = self.fieldofview / 2
        self.height = 2 * math.tan(self.alpha)
        self.width = aspectratio * self.height
        self.pixelwidth = self.width / self.wres
        self.pixelheight = self.height / self.hres

    def calcray(self, x, y):
        xcomp = self.s * (x * self.pixelwidth - self.width / 2)
        ycomp = self.u * (y * self.pixelheight - self.height / 2)
        return Ray(self.e, self.f + xcomp + ycomp)

    def render(self):
        for x in range(self.wres):
            for y in range(self.hres):
                ray = self.calcray(x, y)
                maxdist = float('inf')
                color = self.backgroundcolor
                for object in self.objectlist:
                    hitdist = object.intersectionParameter(ray)
                    if hitdist and hitdist < maxdist:
                        maxdist = hitdist
                        # print(ray)
                        color = (255, 255, 255)
                self.image.putpixel((x, int(self.height - y - 1)), color)