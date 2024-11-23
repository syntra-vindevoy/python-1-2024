# https://www.youtube.com/watch?v=BwWHXN2rZHQ&list=PLhNzqXKONpDXRVV2SySJE2YyMq2t6zQpO&index=18
# soldier position

import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragables")


# Create a rectangle object
rect_1 = pygame.Rect(100, 100, 50, 50)  # x, y, width, height
rect_2 = pygame.Rect(200, 100, 50, 50)
rect_2.left = 500  # left side on coord 500
rect_2.width = 100
# and so on...

# Load an image rectangle
# soldier = pygame.image.load("soldier.png").convert_alpha()
# rect_soldier = soldier.get_rect()


# Create a clock object to control the frame rate
clock = pygame.time.Clock()

run = True

while run:

    # 60 frames per second
    clock.tick(60)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), rect_1)
    pygame.draw.rect(screen, (255, 0, 0), rect_2)

    # screen.blit(soldier, rect_2)
    key = pygame.key.get_pressed()
    if key[pygame.K_q] == True:  # if q pressed
        # rect_2.x -= 5  # move left by five
        rect_2.move_ip(-5, 0)  # move in place
    if key[pygame.K_d] == True:
        rect_2.move_ip(5, 0)
    if key[pygame.K_z] == True:
        rect_2.move_ip(0, -5)
    if key[pygame.K_s] == True:
        rect_2.move_ip(0, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # Update the display
pygame.quit()
