import pygame
import math
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.current_point = 0
        self.health = 1
        self.speed = 2  # примерная скорость
        self.image = pygame.Surface((20, 20))  # create a dummy image for the enemy
        self.image.fill(RED)  # fill the image with a color
        self.rect = self.image.get_rect()  # get the rect of the image
        self.rect.x = self.path.points[0][0]  # set the initial x position
        self.rect.y = self.path.points[0][1]  # set the initial y position

    def update(self):
        current_point = self.path.points[self.current_point]
        if self.current_point + 1 < len(self.path.points):
            next_point = self.path.points[self.current_point + 1]
        else:
            # Enemy has reached the end of the path, stop or reset
            self.rect.x = self.path.points[0][0]; self.rect.y = self.path.points[0][1]
            return

        dx = next_point[0] - current_point[0]
        dy = next_point[1] - current_point[1]
        distance = math.hypot(dx, dy)
        if distance > 0:
            dx /= distance
            dy /= distance
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            if math.hypot(self.rect.x - next_point[0], self.rect.y - next_point[1]) < 5:
                self.current_point += 1