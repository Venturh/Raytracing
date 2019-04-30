import numpy as np
import imageio as im
from Camera import Camera
from Objects.Sphere import Sphere
from Objects.Triangle import Triangle
from Objects.Plane import Plane


width = 400
height = 400
e = np.array([0, 1.8, 10])
c = np.array([0, 3, 0])
up = np.array([0, 1, 0])
fov = 45

image = np.zeros((height, width, 3))
background = np.array([1, 1, 1])

camera = Camera(e, c, up, fov, 1, height, width)
pl = Plane(np.array([0, 0, 0]), np.array([0, 1, 0]))
s1 = Sphere(np.array([3, 1, -1]), 1)
s2 = Sphere(np.array([-3, 1, -1]), 1)
s3 = Sphere(np.array([1.5, 0.5, 1]), 1)
tr = Triangle(np.array([1.5, 0.5, 0.5]), np.array([0, 3, 0.5]), np.array([-1.5, 0.5, 0.5]))
objectlist = []
objectlist.append(pl)
objectlist.append(s1)
objectlist.append(s2)
objectlist.append(s3)
objectlist.append(tr)

for x in range(width):
    for y in range(height):
        ray = camera.calcray(x, y)
        maxdist = float('inf')
        color = background
        for object in objectlist:
            hitdist = object.intersectionParameter(ray)
            if hitdist and hitdist < maxdist:
                maxdist = hitdist
                color = np.array([1/hitdist, 1/hitdist, 1/hitdist])
        image[height - y - 1][x] = color
im.imsave('render.png', image)
print("done")