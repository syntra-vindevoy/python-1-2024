import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Collision")

# text_font = pygame.font.SysFont("Arial", 30)
# text_font = pygame.font.Font("some_font.ttf", bold=True, italic=True)  # font in folder
text_font = pygame.font.SysFont(None, 30, bold=True, italic=True)  # pygame font


def draw_text(text, font, text_col, x, y):
    img = text_font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True
while run:
    screen.fill((0, 0, 0))
    draw_text("Hello World", text_font, (255, 255, 255), 200, 200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
