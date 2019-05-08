import numpy as np
import imageio as im
from Camera import Camera
from Objects.Ray import Ray
from Objects.Sphere import Sphere
from Objects.Triangle import Triangle
from Objects.Plane import Plane
from Objects.Light import Light
from Material import Material
from Material import CheckerBoardMaterial
import threading
import logging


class RayTracing(object):

    def __init__(self):
        self.width = 400
        self.height = 400
        self.e = np.array([0, 1.8, 10])
        self.c = np.array([0, 3, 0])
        self.up = np.array([0, 1, 0])
        self.fov = 45
        self.image = np.zeros((self.height, self.width, 3))
        self.background = np.array([0, 0, 0])

        self.camera = Camera(self.e, self.c, self.up, self.fov, 1, self.height, self.width)
        self.light = Light(np.array([30, 30, 10]), np.array([255, 255, 255]))

        reflecting = True
        checkerboard = True
        self.objectlist = [
            Sphere(np.array([0, 3, 1]), 1, Material(np.array([255, 0, 0]), reflecting)),
            Sphere(np.array([-1.5, 0.5, 1]), 1, Material(np.array([0, 255, 0]), reflecting)),
            Sphere(np.array([1.5, 0.5, 1]), 1, Material(np.array([0, 0, 255]), reflecting)),
            Triangle(np.array([1.5, 0.5, 0.5]), np.array([0, 3, 0.5]), np.array([-1.5, 0.5, 0.5]), Material(np.array([255, 255, 0]), False))
            ]
        if checkerboard:
            plane = Plane(np.array([0, -1, 0]), np.array([0, 1, 0]), CheckerBoardMaterial(False))
        else:
            plane = Plane(np.array([0, -1, 0]), np.array([0, 1, 0]), Material(np.array([128, 128, 128]), False))

        self.objectlist.append(plane)

    def calcColor(self, ray):

        maxdist = float('inf')
        for obj in self.objectlist:
            hitdist = obj.intersectionParameter(ray)
            if hitdist and 0 < hitdist < maxdist:
                break

        if not hitdist:
            return self.background

        objectColor = obj.material.colorAt(ray.intersectionParameter(hitdist))
        phongColor = self.phongMagic(obj, hitdist, ray)
        color = objectColor * phongColor

        if obj.material.reflecting:
            hp = ray.intersectionParameter(hitdist)
            d = ray.direction
            n = obj.normalAt(hp)
            color += self.calcColor(Ray(hp, d - (2 * np.dot(n, d) * n)))

        if self.shadows(ray, hitdist):
            color *= 0.3

        return color

    def phongMagic(self, obj, h, ray):
        hit = ray.intersectionParameter(h)
        n = obj.normalAt(hit)
        direction = ray.direction / np.linalg.norm(ray.direction)

        ca = self.light.color  #Lichtfarbe
        ka = obj.material.ambient  #Materialkonstante
        ambient = ca * ka

        cin = ca
        kd = obj.material.diffuse
        l = (self.light.origin - hit) / np.linalg.norm(self.light.origin - hit)
        ln = np.dot(l, n)
        diffuse = cin * kd * ln

        ks = obj.material.specular
        tmp = (-1) - (2 * np.dot(-1, n) * n)
        lr = tmp/np.linalg.norm(tmp)
        specular = cin * ks * np.dot(lr, -direction)**obj.material.surface

        color = ambient + diffuse + specular
        return color

    def shadows(self, ray, h):
        hit = ray.intersectionParameter(h)
        lightRay = Ray(hit,self.light.origin - hit / np.linalg.norm(self.light.origin - hit))
        maxdist = self.light.distance(lightRay)

        for obj in self.objectlist:
            hitdist = obj.intersectionParameter(lightRay)
            if hitdist and 0.001 <= hitdist <= maxdist:
                return True
        return False

    def worker(self,pool, ray):
        return pool.append(self.calcColor(ray))

    def render(self):
        rays = []
        for x in range(self.width):
            for y in range(self.height):
                rays.append(self.camera.calcray(x, y))

        threads = []
        pool = []
        for ray in rays:
            thread = threading.Thread(target=self.worker(pool, ray))
            threads.append(thread)
            thread.start()
            thread.join()

        i = 0
        for x in range(self.width):
            for y in range(self.height):
                self.image[self.height - y - 1][x] = pool[i]
                i += 1

        im.imsave("render.png", self.image)


if __name__ == "__main__":
    scene = RayTracing()
    scene.render()