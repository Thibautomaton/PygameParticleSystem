
from pygame.math import Vector2 as vector
from Particle import Particle

class ParticleSystem():
    def __init__(self,origin):
        self.origin = vector(origin.x, origin.y)

        self.particles = []

        self.age = 0

        self.gravity = vector(0, 0.1)

    def update_origin(self, origin):
        self.origin = origin

    def run(self):
        self.age+=1
        for p in self.particles:
            p.applyForce(self.gravity)
            p.run()

        self.particles = [p for p in self.particles if not p.isDead()]

    def isDead(self):
        if self.age>500:
            return True
        else:
            return False


    def addParticle(self):
        self.particles.append(Particle(self.origin))
