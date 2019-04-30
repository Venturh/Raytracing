import numpy as np

from PIL import Image as im
from Camera import Camera
from Objects.Sphere import Sphere
from Objects.Triangle import Triangle
from Objects.Plane import Plane
import Phong as ph

rot = ph.Phong(np.array([255, 0, 0]))

objectlist = [
    Sphere(np.array([0, 3, 1]), 1, None),
    Sphere(np.array([-1.5, 0.5, 1]), 1, None),
    Sphere(np.array([1.5, 0.5, 1]), 1, None),
    Triangle(np.array([1.5, 0.5, 0.5]), np.array([0, 3, 0.5]), np.array([-1.5, 0.5, 0.5]), None),
    Plane(np.array([0, -1, 0]), np.array([0, 1, 0]), None)
]
e = np.array([0, 1.8, 10])
c = np.array([0,3, 0])
up = np.array([0, 1, 0])
im = im.new("RGB", (400, 400),(0,0,0))
fow = 45
aspect = 400/400

camera = Camera(e,c,up,aspect,fow,400,400,objectlist,im,np.array([0, 0, 0]))
camera.render()
final = camera.image
final.show()
