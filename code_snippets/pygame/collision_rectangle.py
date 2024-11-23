# https://www.youtube.com/watch?v=BHr9jxKithk&list=PLhNzqXKONpDXRVV2SySJE2YyMq2t6zQpO&index=22


import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Collision")

rect_1 = pygame.Rect(100, 100, 50, 50)

obstacles = []
for _ in range(10):
    obstacle_rect = pygame.Rect(randint(0, 500), randint(0, 500), 20, 20)
    obstacles.append(obstacle_rect)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pygame.mouse.set_visible(False)

run = True
while run:

    screen.fill(BG)
    col = GREEN
    if (collide := rect_1.collidelist(obstacles)) >= 0:
        print(collide)
        col = RED
    for obstacle in obstacles:
        if rect_1.colliderect(obstacle):
            col = RED

    pos = pygame.mouse.get_pos()
    rect_1.center = pos

    pygame.draw.rect(screen, col, rect_1)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLUE, obstacle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
