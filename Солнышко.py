import random
import math
import pygame
import sys
import turtle

pygame.init()
screen = pygame.display.set_mode([800,800])
screen2 = pygame.display.set_mode([800,800])
pic = pygame.image.load('image.png')
picx = 0
picy = 0
t = turtle.Pen()
t.speed(0)

# import pygame
# import sys

# pygame.init()

# screen = pygame.display.set_mode((1200, 800))

while True:
    for i in range(1000):
        t.fd(i)
        t.rt(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    i = random.randint(0,800)
    q = random.randint(0,800)
    screen.blit(pic,(picx + i, picy + q))
    screen2.blit(pic,(picx + q, picy + i))
    pygame.display.update()