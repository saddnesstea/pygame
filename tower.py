import pygame
from settings import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, tower_type, enemies, bullets, all_sprites):
        super().__init__()
        self.image = pygame.Surface((TOWER_SIZE, TOWER_SIZE))
        self.image.fill(TOWER_COLOR)
        self.rect = self.image.get_rect(center=(x, y))
        self.tower_type = tower_type
        self.enemies = enemies
        self.bullets = bullets
        self.all_sprites = all_sprites
        self.shoot_interval = TOWER_TYPES[tower_type]['shoot_interval']
        self.last_shot_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_interval:
            self.last_shot_time = current_time
            self.shoot()

    def shoot(self):
        # Find the closest enemy
        closest_enemy = None
        closest_distance = float('inf')
        for enemy in self.enemies:
            distance = self.rect.distance_to(enemy.rect)
            if distance < closest_distance:
                closest_enemy = enemy
                closest_distance = distance

        if closest_enemy:
            # Create a bullet
            bullet = Bullet(self.rect.center, closest_enemy.rect.center)
            self.bullets.add(bullet)
            self.all_sprites.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.target = target
        self.speed = 2

    def update(self):
        direction = (pygame.Vector2(self.target.rect.center) - pygame.Vector2(self.rect.center)).normalize()
        self.rect.center += direction * self.speed
        if pygame.sprite.collide_rect(self, self.target):
            self.target.health -= 10
            if self.target.health <= 0:
                self.target.kill()
            self.kill()

class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SHOP_WIDTH, SHOP_HEIGHT))
        self.image.fill(SHOP_COLOR)
        self.rect = self.image.get_rect(topleft=(SHOP_X, SHOP_Y))
        self.selected_tower = None

    def update(self):
        # Draw the shop interface
        self.image.fill(SHOP_COLOR)
        font = pygame.font.Font(None, 24)
        for i, tower_type in enumerate(TOWER_TYPES):
            text = font.render(f"{tower_type}: {TOWER_TYPES[tower_type]['cost']}", True, WHITE)
            self.image.blit(text, (10, 10 + i * 30))

        # Draw the selected tower's information
        if self.selected_tower:
            text = font.render(f"Selected: {self.selected_tower}", True, WHITE)
            self.image.blit(text, (10, SHOP_HEIGHT - 30))

    def get_selected_tower(self):
        return self.selected_tower

    def select_tower(self, tower_type):
        self.selected_tower = tower_type
