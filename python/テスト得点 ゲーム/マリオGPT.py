import pygame
import random
import sys

# 初期設定
pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Maze Generator")
clock = pygame.time.Clock()

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# 迷路の設定
cols = WIDTH // GRID_SIZE
rows = HEIGHT // GRID_SIZE

# 迷路を初期化
maze = [[0 for _ in range(cols)] for _ in range(rows)]

def draw_maze():
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Grid lines

def generate_maze():
    stack = []
    start_cell = (random.randint(0, cols - 1), random.randint(0, rows - 1))
    stack.append(start_cell)
    maze[start_cell[1]][start_cell[0]] = 1  # Mark start cell as visited

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left

    while stack:
        current = stack[-1]
        cx, cy = current
        neighbors = []

        for direction in directions:
            nx, ny = cx + direction[0] * 2, cy + direction[1] * 2
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == 0:
                neighbors.append((nx, ny))

        if neighbors:
            next_cell = random.choice(neighbors)
            nx, ny = next_cell
            maze[ny][nx] = 1
            maze[(cy + ny) // 2][(cx + nx) // 2] = 1
            stack.append(next_cell)
        else:
            stack.pop()

# メインループ
generate_maze()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    draw_maze()
    pygame.display.flip()
    clock.tick(30)
