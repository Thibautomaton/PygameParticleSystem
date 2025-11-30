# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pygame
from settings import *
from ParticleSystem import ParticleSystem
from pygame.math import Vector2 as vector

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame particles")

clock = pygame.time.Clock()

systems = []



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0,0,0))

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

        systems.append(ParticleSystem(vector(x, y)))



    for ps in systems:
        if not ps.isDead():
            ps.addParticle()
            ps.run()
        else:
            print(ps.age)
            systems = [ps for ps in systems if not ps.isDead()]

    clock.tick(TARGET_FPS)
    pygame.display.update()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
