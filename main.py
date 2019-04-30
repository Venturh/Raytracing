import numpy as np

from PIL import Image as im
from Camera import Camera
from Objects.Sphere import Sphere
from Objects.Triangle import Triangle
from Objects.Plane import Plane
import Phong as ph

rot = ph.Phong(np.array([255, 0, 0]))

ebene = Plane(np.array([0,-1,0]), np.array([0,1,0]),rot)
kugel = Sphere(np.array([0, 3, 1]), 1,(255,0,0))
kugel2 = Sphere(np.array([0, 6, 1]), 1,(0,0,255))
e = np.array([0, 1.8, 10])
c = np.array([0,3, 0])
up = np.array([0, 1, 0])
im = im.new("RGB", (400, 400),(0,0,0))
fow = 45
aspect = 400/400
objectlist = []

camera = Camera(e,c,up,aspect,fow,400,400,objectlist,im,(0,0,0))
#objectlist.append(ebene)
objectlist.append(kugel)
#objectlist.append(kugel2)
camera.render()
final = camera.image
final.show()