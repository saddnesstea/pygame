import pygame
from math import sqrt
import sys

pygame.init()

LINE_WIDTH = 15
WIDTH, HEIGHT = 600, 600
BG_COLOR = (28, 170, 156)
LINE_COLOR = (64, 134, 97)
CIRCLE_COLOR = (0, 0, 0)
CIRCLE_RADIUS = WIDTH // 9
CROSS_COLOR = (100, 100, 100)
# CROSS_WIDTH = sqrt(((WIDTH // 3) ** 2) * 2) - 50
CROSS_WIDTH = 25
SPACE = WIDTH // 12

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(BG_COLOR)

board = [[0] * 3 for _ in range(3)]

def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(screen,  CIRCLE_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), CIRCLE_RADIUS)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + HEIGHT // 3 - SPACE), (col * WIDTH // 3 + WIDTH // 3 - SPACE, row * HEIGHT // 3 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + SPACE), (col * WIDTH // 3 + WIDTH // 3 - SPACE, row * HEIGHT // 3 + HEIGHT // 3 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[col][0] == board[col][1] == board[col][2] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

draw_lines()
player = 1
game_over = False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            col = event.pos[0] // (WIDTH // 3)
            row = event.pos[1] // (HEIGHT // 3)
            if available_square(row, col):
                mark_square(row, col, player)
                if check_win(player):
                    game_over = True
                player = 2 if player == 1 else 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    pygame.display.update()
