import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Block-Building Game")

clock = pygame.time.Clock()

# Create a 2D grid to represent the blocks
grid = [[0] * (WIDTH // GRID_SIZE) for _ in range(HEIGHT // GRID_SIZE)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button (place block)
                x, y = event.pos
                grid[y // GRID_SIZE][x // GRID_SIZE] = 1
            elif event.button == 3:  # Right mouse button (remove block)
                x, y = event.pos
                grid[y // GRID_SIZE][x // GRID_SIZE] = 0

    # Draw everything
    screen.fill(WHITE)

    # Draw the blocks
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 1:
                pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()
    clock.tick(60)
