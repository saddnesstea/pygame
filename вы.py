import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = path.points[0]
        self.path = path
        self.path_index = 0
        self.speed = 20
        self.health = 100
        self.update_target()

    def update_target(self):
        if self.path_index < len(self.path.points):
            self.target = pygame.Vector2(self.path.points[self.path_index])
        else:
            self.target = None

    # def update(self):
    #     if self.target:
    #         direction = pygame.Vector2(self.target - pygame.Vector2(self.rect.topleft))
    #         if direction.length() != 0:
    #             direction = direction.normalize()
    #             self.rect.topleft += direction * self.speed
    #             if pygame.Vector2(self.rect.topleft).distance_to(self.target) < self.speed:
    #                 self.path_index += 1
    #                 self.update_target()
    #         else:
    #             self.kill()
    #     else:
    #         self.kill()
def update(self):
    if self.target:
        direction = pygame.Vector2(self.target - pygame.Vector2(self.rect.topleft))
        if direction.length() != 0:
            direction = direction.normalize()
            self.rect.topleft += direction * self.speed
            if pygame.Vector2(self.rect.topleft).distance_to(self.target) < self.speed:
                self.path_index += 1
                self.update_target()
        else:
            self.path_index += 1
            self.update_target()
    else:
        # Enemy has reached the end of the path, do something here
        pass