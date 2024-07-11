# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (225, 165, 0)
FPS = 60
TOWER_SIZE = 199
TOWER_COLOR = (24, 231, 94)
SHOP_WIDTH = 199
SHOP_HEIGHT = 199
SHOP_COLOR = (99,87,124)
SHOP_X = 0
SHOP_Y = 0
# Пути
PATH_POINTS = [(0, 300), (200, 300), (200, 500), (600, 500), (600, 100), (800, 100)]
# PATH_POINTS = [(0, 300), (300, 300), (-200, 500), (600, 500)]
# Настройки врагов
ENEMY_TYPES = {
    'basic': {'speed': 3, 'health': 100, 'color': RED},
    'fast': {'speed': 4, 'health': 50, 'color': GREEN},
    'tank': {'speed': 1, 'health': 200, 'color': BLUE}
}

# Настройки башен
TOWER_TYPES = {
    'basic': {'range': 100, 'fire_rate': 1000, 'cost': 50, 'color': BLUE},
    'sniper': {'range': 2000, 'fire_rate': 2000, 'cost': 100, 'color': YELLOW},
    'rapid': {'range': 50, 'fire_rate': 500, 'cost': 75, 'color': GREEN}
}