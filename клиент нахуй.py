import socket
import pygame
import sys
import threading

# Настройки Pygame
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
CIRCLE_RADIUS = WIDTH // 6
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = WIDTH // 12

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-Нолики Клиент')
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
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), CIRCLE_RADIUS, CIRCLE_WIDTH)
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
        if board[0][col] == board[1][col] == board[2][col] == player:
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

# Настройки клиента
HOST = 'сервер_айпи'
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

player = 2
game_over = False

def receive_data():
    global player, game_over
    while True:
        data = client_socket.recv(1024).decode()
        if data == 'restart':
            restart()
            player = 2
            game_over = False
        else:
            row, col = map(int, data.split(','))
            mark_square(row, col, 1 if player == 2 else 2)
        draw_figures()
        pygame.display.update()

threading.Thread(target=receive_data).start()

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            col = event.pos[0] // (WIDTH // 3)
            row = event.pos[1] // (HEIGHT // 3)
            if available_square(row, col):
                mark_square(row, col, player)
                if check_win(player):
                    game_over = True
                client_socket.sendall(f"{row},{col}".encode())
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 2
                game_over = False
                client_socket.sendall('restart'.encode())
    pygame.display.update()
