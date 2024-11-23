# https://www.youtube.com/watch?v=BHr9jxKithk&list=PLhNzqXKONpDXRVV2SySJE2YyMq2t6zQpO&index=22


import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Collision")

rect_1 = pygame.Rect(100, 100, 50, 50)
obstacle_rect = pygame.Rect(randint(0, 500), randint(0, 500), 20, 20)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
