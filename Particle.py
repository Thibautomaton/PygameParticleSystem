import pygame.draw
from pygame.math import Vector2 as vector
import random

class Particle():
    def __init__(self, position):
        self.r = 5

        self.location = vector(position.x, position.y)
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)

        self.display_surface = pygame.display.get_surface()


        self.aVelocity = 0.25
        self.aAcceleration = 0

        self.angle = 0
        self.lifespan = 255

        self.applyForce(vector(random.uniform(-5, 5), random.uniform(-5, 0)))

    def update(self):
        self.velocity +=self.acceleration
        self.location +=self.velocity

        self.acceleration*=0

        self.aVelocity += self.aAcceleration
        self.angle += self.aVelocity

        self.aAcceleration *=0

        self.lifespan  -=2

    def display(self):
        color = (175, 175, 175)
        # pygame.draw.circle(self.display_surface, color, self.location, self.r)

        border = (255, 255, 255)
        size = self.r *2

        surface = pygame.Surface((size, size), pygame.SRCALPHA)

        rect = pygame.Rect(0, 0, size, size)

        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, border, rect, 2)

        rotated_surf = pygame.transform.rotate(surface, self.angle)

        rotated_rect = rotated_surf.get_rect(center = (self.location.x, self.location.y))

        self.display_surface.blit(rotated_surf, rotated_rect)


    def applyForce(self, force):
        self.acceleration += force

        self.aAcceleration += random.uniform(-2, 2)

    def run(self):
        self.update()
        self.display()

    def isDead(self):
        if self.lifespan<0:
            return True
        else:
            return False



