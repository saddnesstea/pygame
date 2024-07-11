import pygame
from settings import *
from enemy import Enemy
from tower import Tower, Shop
from path import Path

# # Инициализация Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Tower Defense")
# screen.fill(WHITE)
# # # Группы спрайтов
# all_sprites = pygame.sprite.Group()
# enemies = pygame.sprite.Group()
clock = pygame.time.Clock()
# towers = pygame.sprite.Group()
# bullets = pygame.sprite.Group()

# # # Создание пути
# path = Path(PATH_POINTS)

# # Создание врагов
enemy_spawn_interval = 3000  # initial spawn interval
def spawn_enemy():
    global enemy_spawn_interval
    enemy = Enemy(path)
    all_sprites.add(enemy)
    enemies.add(enemy)
    print(f"Enemy spawned! Total enemies: {len(enemies)}")
    if enemy_spawn_interval - 100 != 200:
        enemy_spawn_interval -= 100  # decrease spawn interval by 100ms each wave

# # Начальная волна врагов
# for _ in range(5):
#     spawn_enemy()

# # Создание магазина
# shop = Shop()
# all_sprites.add(shop)

# # Деньги игрока
# player_money = 10000

# # Главный игровой цикл
# last_enemy_spawn_time = 0
# while True:
#     font = pygame.font.Font(None, 24)
#     text = font.render(f"Money: {player_money}", True, WHITE)
#     screen.blit(text, (10, 10))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if True:
#                 tower_type = shop.get_selected_tower()
#                 if tower_type and player_money >= TOWER_TYPES[tower_type]['cost']:
#                     x, y = event.pos
#                     tower = Tower(x, y, tower_type, enemies, bullets, all_sprites)
#                     all_sprites.add(tower)
#                     towers.add(tower)
#                     player_money -= TOWER_TYPES[tower_type]['cost']

#     current_time = pygame.time.get_ticks()
#     if current_time - last_enemy_spawn_time >= enemy_spawn_interval:
#         last_enemy_spawn_time = current_time
#         spawn_enemy()

#     all_sprites.update()
    
#     screen.fill(WHITE)
#     path.draw(screen)
#     all_sprites.draw(screen)
#     pygame.display.flip()
#     pygame.display.update()
#     clock.tick(FPS)

import pygame
from settings import *
from enemy import Enemy
from tower import Tower, Shop
from path import Path

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")
screen.fill(WHITE)

# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
towers = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Создание пути
path = Path(PATH_POINTS)

# Создание магазина
shop = Shop()
all_sprites.add(shop)

# Деньги игрока
player_money = 10000

# Главный игровой цикл
def game_loop():
    last_enemy_spawn_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if True:
                    tower_type = shop.get_selected_tower()
                    if tower_type and player_money >= TOWER_TYPES[tower_type]['cost']:
                        x, y = event.pos
                        tower = Tower(x, y, tower_type, enemies, bullets, all_sprites)
                        all_sprites.add(tower)
                        towers.add(tower)
                        player_money -= TOWER_TYPES[tower_type]['cost']

        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn_time >= enemy_spawn_interval:
            last_enemy_spawn_time = current_time
            spawn_enemy()

        all_sprites.update()

        screen.fill(WHITE)
        path.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

        # Check for game over
        if len(enemies) == 0:
            game_over()

def game_over():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 24))
    pygame.display.flip()
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()

def start_menu():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 48)
    text = font.render("Tower Defense", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 24))
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_loop()

start_menu()