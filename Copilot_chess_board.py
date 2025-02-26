import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# Define Colors
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)

# Draw Chessboard
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_board()
    pygame.display.update()

pygame.quit()
