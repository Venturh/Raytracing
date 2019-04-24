import numpy as np
import math

HINTERGRUNDFARBE = 0
FIELDOFVIEW = 45
ASPECTRATIO = 10

# Kamera
e = np.array([0, 1.8, 10])
c = np.array([0, 3, 0])
up = np.array([0, 1, 0])

# Koordinatensystem
cminusE = c - e
f = cminusE / math.sqrt(cminusE[0] ** 2 + cminusE[1] ** 2 + cminusE[2] ** 2)
fKreuzUp = np.cross(f, up)
s = fKreuzUp / math.sqrt(fKreuzUp[0] ** 2 + fKreuzUp[1] ** 2 + fKreuzUp[2] ** 2)
u = np.cross(s,f)


def calcray(x, y):
    return 0


# Betrachtergeometrie
alpha = FIELDOFVIEW / 2
w = 400
w = 400

height = 2 * math.tan(alpha)
width = ASPECTRATIO * height

wRes = 400
hRes = 400


pixelWidth = width / (wRes - 1)
pixelHeight = height / (hRes - 1)
for y in range(hRes):
    for x in range(wRes):
        xcomp = s.scale(x * pixelWidth - width / 2)
        ycomp = s.scale(y * pixelHeight - height / 2)
        ray = Ray(e, f + xcomp + ycomp)

# RayCasting
for x in range(400):
    for y in range(400):
        ray = calcray(x, y)
        maxdist = float('inf')
        farbe = HINTERGRUNDFARBE
        for object in objectlist:
            hitdist = object.intersectionParameter(ray)
            if hitdist:
                if hitdist < maxdist:
                    maxdist = hitdist
                    farbe = object.colorAt(ray)
        image.putpixel((x, y), farbe)
