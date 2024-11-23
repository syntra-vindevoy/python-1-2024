# https://www.youtube.com/watch?v=Ro82dac_J1Y

import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragables")

active_box = None  # cwhich box is being dragged
boxes = []

for _ in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = random.randint(35, 65)
    h = random.randint(35, 65)
    box = pygame.Rect(x, y, w, h)
    boxes.append(box)

run = True
while run:
    screen.fill((0, 0, 0))

    for box in boxes:
        pygame.draw.rect(screen, (255, 0, 0), box)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None
        if event.type == pygame.MOUSEMOTION:
            if active_box is not None:
                boxes[active_box].move_ip(event.rel)
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()  # Update the display

pygame.quit()
