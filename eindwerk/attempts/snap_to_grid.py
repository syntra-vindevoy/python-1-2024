import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 50  # Define the grid size

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragables")

active_box = None  # which box is being dragged
boxes = []

for _ in range(5):
    x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    w = random.randint(1, 2) * GRID_SIZE
    h = random.randint(1, 2) * GRID_SIZE
    box = pygame.Rect(x, y, w, h)
    boxes.append(box)

def snap_to_grid(rect):
    rect.x = round(rect.x / GRID_SIZE) * GRID_SIZE
    rect.y = round(rect.y / GRID_SIZE) * GRID_SIZE

run = True
while run:
    screen.fill((0, 0, 0))

    for box in boxes:
        pygame.draw.rect(screen, (255, 0, 0), box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                for box in boxes:
                    if box.collidepoint(event.pos):
                        active_box = box
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # left click
                if active_box:
                    snap_to_grid(active_box)
                active_box = None
        elif event.type == pygame.MOUSEMOTION:
            if active_box:
                active_box.move_ip(event.rel)

    pygame.display.flip()

pygame.quit()