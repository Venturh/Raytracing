import numpy as np
from PIL import Image as im
import math
import Hilfsklassen
import Klassen



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

        temp = self.c - self.e
        self.f = self.c-self.e / np.linalg.norm(temp)
        temp = np.cross(self.f, self.up)
        self.s = temp / np.linalg.norm(temp)
        self.u = np.cross(self.f, self.s)

        self.alpha = self.fieldofview / 2
        self.height = 2 * math.tan(self.alpha)
        self.width = aspectratio * self.height
        self.pixelwidth = self.width / self.wres
        self.pixelheight = self.height / self.hres

        self.render()

    def calcray(self, x, y):
        xcomp = self.s * ((x * self.pixelwidth) - (self.width / 2))
        ycomp = self.u * ((y * self.pixelheight) - (self.height / 2))
        return Klassen.Ray(self.e, self.f + xcomp + ycomp)

    def render(self):
        for x in range(self.wres):
            for y in range(self.hres):
                ray = self.calcray(x, y)
                maxdist = float('inf')
                color = self.backgroundcolor
                for objekt in self.objectlist:
                    hitdist = objekt.intersectionParameter(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            print(ray)
                            #color = (200,0,0)
                self.image.putpixel((x, y), color)


ebene = Klassen.Plane(np.array([0,1,0]), np.array([1,1,1]))
e = np.array([0, 1.8, 10])
c = np.array([0,3, 0])
up = np.array([0, 1, 0])
im = im.new("RGB", (400, 400))
fow = 45
aspect = 400/400
objectlist = [ebene]

camera = Camera(e,c,up,aspect,fow,400,400,objectlist,im,(0,0,0))
final = camera.image
final.show()











