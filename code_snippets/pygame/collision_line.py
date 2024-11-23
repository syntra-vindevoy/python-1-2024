# https://www.youtube.com/watch?v=BHr9jxKithk&list=PLhNzqXKONpDXRVV2SySJE2YyMq2t6zQpO&index=22


import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Collision")
obstacles = []
for _ in range(10):
    obstacle_rect = pygame.Rect(randint(0, 500), randint(0, 500), 20, 20)
    obstacles.append(obstacle_rect)

line_start = (SCREEN_WIDTH / 2, SCREEN_HEIGTH / 2)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

run = True
while run:
    screen.fill(BG)
    pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, WHITE, line_start, pos, 5)
    for obstacle in obstacles:
        if obstacle.clipline(line_start, pos):
            pygame.draw.rect(screen, RED, obstacle)
        else:
            pygame.draw.rect(screen, GREEN, obstacle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
